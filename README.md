# About
- Script will download youtube video in both mp3 and mp4 formats in the highest resolution possible. 
- Input a url and output file name.

# Tested on
- Windows 10

- Linux

# How to use

- git clone https://github.com/udit19281/youtube-video-downloader.git

- pip install -r requirements.txt

- python downloade.py


# Known Error and handling

Error : 'cipher'

update line 300 of extract.py (pytube folder inside site-packages of python lib) as follows :

except KeyError:
cipher_url = [
parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats) if "signatureCipher" in formats[i]
]




