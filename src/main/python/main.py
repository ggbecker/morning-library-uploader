from fbs_runtime.application_context.PyQt5 import ApplicationContext
import sys
import os
import mutagen
import requests


from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtCore import QFile
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.lastAddedFolder = None
        self.lineEditMusicFolder.setDisabled(True)

    def uploadTracks(self):
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.lineEditMusicFolder.text()):
            for file in f:
                if '.flac' in file or '.mp3' in file or '.wav' in file or '.aiff' in file or '.ape' in file:
                    tag = mutagen.File(os.path.join(r, file))
                    if tag is not None:
                        myobj =  {'title': str(*tag.get('title', []))}
                        myobj.update({'album': str(*tag.get('album', []))})
                        myobj.update({'artist': str(*tag.get('artist', []))})
                        myobj.update({'year': str(*tag.get('date', []))})
                        myobj.update({'location': 'Files (D:)'})
                        myobj.update({'path': os.path.abspath(os.path.join(r, file))})
                        myobj.update({'length': str(tag.info.length)})
                        myobj.update({'sample_rate': str(tag.info.sample_rate)})
                        # myobj.update({'bits_per_sample': str(tag.info.bits_per_sample)})
                        myobj.update({'bitrate': str(tag.info.bitrate)})
                        myobj.update({'codec': str(type(tag).__name__)})

                        url = 'http://127.0.0.1:8000/api/track/'
                        # url = 'http://morning-library-morning-library.2886795280-80-host04nc.environments.katacoda.com/api/track/'
                        # url = 'http://ec2-3-132-215-58.us-east-2.compute.amazonaws.com/api/track/'

                        x = requests.post(url, data = myobj, headers={'Authorization': 'Token {}'.format(self.lineEditApiToken.text())}, verify=False)
                        print(x.text)
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
