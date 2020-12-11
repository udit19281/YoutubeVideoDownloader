
from moviepy.editor import *
import os
from time import sleep
import sys
def install_and_import(package):        # Function Reference: stackoverflow
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        print("INSTALLING PYTUBE")
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import('pytube')
from pytube import YouTube
link=input("ENTER LINK OF THE VIDEO : ")
try:
    yt2= YouTube(link)
    yt=yt2.streams.filter(progressive=True)
    video=yt2.streams.get_highest_resolution()
except Exception as e:
    print(e)
    print("ERROR TRY AGAIN")
    exit()

path=os.getcwd()
name=input("ENTER VIDEO TITLE (without '/,|,mp3,mp4') eg:VIDEO_NAME :")

if name!="":
    audiotodown=yt[0]
    print("[+] DOWNLOADING REQUIRED FILES WAIT... ")
    try:
        video.download(path,"v1")
        audiotodown.download(path,"a1")
    except:
        print(f"PATH NOT FOUND {path}: ".format(path))
        exit()
    print("[+] DOWNLOADED FILES")
    print("[+] CONVERTING FILES PLEASE WAIT ...")

    # Converting downloaded files

    vid=VideoFileClip(path+r"\v1.mp4")
    aud=VideoFileClip(path+r"\a1.mp4")
    audmp3=aud.audio
    audmp3.write_audiofile(path+r"\r"+name+".mp3",verbose=False)
    #exit()
    namevid=path+r"\r"+name+".mp4"
    try:
        vid.write_videofile(namevid,audio=path+r"\r"+name+".mp3",verbose=False)
    except Exception as e:
        print (e)
        vid.close()
        aud.close()
        audmp3.close()
        os.remove(path+r"\v1.mp4")
        os.remove(path+r"\r"+name+".mp3")
        os.remove(path+r"\a1.mp4")
        exit()

    vid.close()
    aud.close()
    audmp3.close()
    #command to remove extra downloaded files
    print("[+] REMOVING EXTRA FILES ...")
    os.remove(path+r"\v1.mp4")
    #os.remove(path+r"\a2.mp3")
    os.remove(path+r"\a1.mp4")

    print(f"[+] VIDEO DOWNLOADED AT: {path} WITH NAME: {name} ".format(path=path, name=namevid))

#Code By: udit19281
