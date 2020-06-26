from fbs_runtime.application_context.PyQt5 import ApplicationContext
import sys
import os
import mutagen
import requests

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

audio_formats = ('.3gp'
,'.aa'
,'.aac'
,'.aax'
,'.act'
,'.aiff'
,'.alac'
,'.amr'
,'.ape'
,'.au'
,'.awb'
,'.dct'
,'.dss'
,'.dvf'
,'.flac'
,'.gsm'
,'.ikla'
,'.ivs'
,'.m4a'
,'.m4b'
,'.m4p'
,'.mmf'
,'.mp3'
,'.mpc'
,'.msv'
,'.nmf'
,'.nsf'
,'.ogg'
,'.opus'
,'.ra'
,'.raw'
,'.rf64'
,'.sln'
,'.tta'
,'.voc'
,'.vox'
,'.wav'
,'.wma'
,'.wv'
,'.webm'
,'.8svx'
,'.cda'
)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.lastAddedFolder = None
        self.lineEditMusicFolder.setDisabled(True)

    def uploadTracks(self):
        url = 'https://morninglibrary.ignorelist.com/api/track/'
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.lineEditMusicFolder.text()):
            for file in f:
                if file.endswith(audio_formats):
                    tag = mutagen.File(os.path.join(r, file))
                    if tag is not None:
                        myobj =  {'title': ', '.join(tag.get('title', []))}
                        myobj.update({'album': ', '.join(tag.get('album', []))})
                        myobj.update({'artist': ', '.join(tag.get('artist', []))})
                        myobj.update({'year': ', '.join(tag.get('date', []))})
                        myobj.update({'location': ' '})
                        myobj.update({'path': os.path.abspath(os.path.join(r, file))})
                        myobj.update({'length': str(tag.info.length)})
                        myobj.update({'sample_rate': str(tag.info.sample_rate)})
                        # myobj.update({'bits_per_sample': str(tag.info.bits_per_sample)})
                        myobj.update({'bitrate': str(tag.info.bitrate)})
                        myobj.update({'codec': str(type(tag).__name__)})

                        x = requests.post(url, data = myobj, headers={'Authorization': 'Token {}'.format(self.lineEditApiToken.text())})
                        self.textBrowserOutput.append(x.text)

    def browse(self):
        title = self.tr("Select a folder to upload")
        flags = QFileDialog.ShowDirsOnly
        dirpath = str(QFileDialog.getExistingDirectory(self, title, self.lastAddedFolder, flags))
        if not dirpath:
            return
        self.lastAddedFolder = dirpath
        self.lineEditMusicFolder.setText(dirpath)

    def about(self):
        about = QWidget()
        about.resize(320, 240)
        about.show()

if __name__ == "__main__":
    appctxt = ApplicationContext()

    window = MainWindow()
    window.show()

    sys.exit(appctxt.app.exec_())
