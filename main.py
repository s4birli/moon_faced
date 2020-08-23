from getFrames import *
from difference import *
from youtubeClass import *
pathIn="D:\\Source Codes\\moon_faced\\Video\\video.mp4"
pathOut="D:\\Source Codes\\moon_faced\\Frames\\"
##getImages(pathIn, pathOut)
##compare_frames(pathOut)

def start_project():    
    print("*********** Welcome *************")
    print("What would you like to do?")
    print("1. Download File?")
    print("2. Split Video?")
    print("3. Create Video")
    print()
    val = int(input(""))
    if val == 1:
        url = str(input("Please give me URL: "))
        downloadFile(url)
        start_project()
    if val == 2:
        # save each frames
        # control frames 
        # get start second point
        # if frame is above ** then check frequency 
        # if frame is above ** and if frequency is diffrenct
        # add to array start and end point
        # after all split the video!
        # add details to json file (mongodb) title, create date, index, added before?
        start_project()
    if val == 3:
        # manuel? auto?
        # if manuel want all list or undone or done?
        # min minute?
        # get id of clips
        # add them all together

        # if auto want random or undone or done?
        # min minute?
        # add them all together
        start_project()

start_project()