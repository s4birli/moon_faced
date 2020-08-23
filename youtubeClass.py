from pytube import YouTube
import sys
import os

def downloadFile(url):
    try:
        youtube = YouTube(url)
        video = youtube.streams.first()
        filename = os.getcwd() + "/Video"
        video.download(filename) # path, where to video download.
        print ("File Downloaded!")
    except:
        print("Unexpected error:", sys.exc_info()[0])
    