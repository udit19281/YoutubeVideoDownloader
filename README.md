# About
this python script will download youtube videos using a url in the highest resolution possible. give it a url,path to the folder and final video name.

# Tested on
- Windows

- Linux

# How to use

- git clone https://github.com/udit19281/youtube-video-downloader.git

- pip install -r requirements.txt

- python youtube_video_downloader.py

# Known Error and handling

Error : 'cipher'

update line 300 of extract.py (pytube folder inside site-packages of python lib) as follows :

except KeyError:
cipher_url = [
parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats) if "signatureCipher" in formats[i]
]




