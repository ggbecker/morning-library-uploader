import os
import sys
import mutagen
import requests
from glob import glob

files = [y for x in os.walk('.') for y in glob(os.path.join(x[0], '*.flac'))]
files2 = [y for x in os.walk('.') for y in glob(os.path.join(x[0], '*.mp3'))]

for file in files+files2:
    if os.path.isfile(file):
        tag = mutagen.File(file)
        if tag is not None:
            print("tag is not none")
            print(os.path.abspath(file))

            # print(tag)
            
            myobj =  {'title': str(*tag.get('title', []))}
            myobj.update({'album': str(*tag.get('album', []))})
            myobj.update({'artist': str(*tag.get('artist', []))})
            myobj.update({'year': str(*tag.get('date', []))})
            myobj.update({'location': 'disco1'})
            myobj.update({'path': os.path.abspath(file)})
            myobj.update({'length': str(tag.info.length)})
            myobj.update({'sample_rate': str(tag.info.sample_rate)})
            # myobj.update({'bits_per_sample': str(tag.info.bits_per_sample)})
            myobj.update({'bitrate': str(tag.info.bitrate)})
            myobj.update({'codec': str(type(tag).__name__)})
            myobj.update({'owner': 'gabriel'})

            url = 'http://127.0.0.1:8000/api/track/'

            x = requests.post(url, data = myobj)

            print(x.text)


