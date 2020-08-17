from pytube import YouTube
from moviepy.editor import *
import os
import sys
link=input("ENTER LINK OF THE VIDEO : ")
try:
    yt2= YouTube(link)
    yt=yt2.streams.filter(progressive=True)
    video=yt2.streams.get_highest_resolution()
except:
    print("ERROR TRY AGAIN")
    exit()

def_path="C:/Users/Dell/Downloads"   #update your file path here

path=input(f"ENTER PATH TO DOWNLOAD THE VIDEO (ENTER for default : {def_path}) : ".format(def_path=def_path))

if path=="":
    path=def_path

name=input("ENTER VIDEO TITLE (without '/,|,mp3,mp4') eg:VIDEO_NAME :")

if name!="":
    audiotodown=yt[0]
    print("[+] DOWNLOADING REQUIRED FILES WAITZ.. ")
    try:
        video.download(path,"v1")
        audiotodown.download(path,"a1")
    except:
        print(f"PATH NOT FOUND {path}: ".format(path))
        exit()
    print("[+] DOWNLOADED FILES")
    print("[+] CONVERTING FILES PLEASE WAIT ...")

    #converting downloaded files 

    vid=VideoFileClip(path+"/v1.mp4")
    aud=VideoFileClip(path+"/a1.mp4")
    audmp3=aud.audio
    audmp3.write_audiofile(path+"/a2.mp3",verbose=False)

    name=path+"/"+name+".mp4"
    try:
        vid.write_videofile(name+".mp4",audio=path+"/a2.mp3")
    except Exception as e:
        print (e)
        vid.close()
        aud.close()
        audmp3.close()
        os.remove(path+"/v1.mp4") 
        os.remove(path+"/a2.mp3")
        os.remove(path+"/a1.mp4")
        exit()

    vid.close()
    aud.close()
    audmp3.close()
    #command to remove extra downloaded files
    print("[+] REMOVING EXTRA FILES ...")
    os.remove(path+"/v1.mp4") 
    os.remove(path+"/a2.mp3")
    os.remove(path+"/a1.mp4")

    print(f"[+] VIDEO DOWNLOADED at {path} with name {name} ".format(path=path, name=name))
