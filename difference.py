import cv2
import os
from os.path import isfile, join
from diffimg import diff
import os.path
from os import path

def compare_frames(pathOut):
    ''' this function coverts images to video '''
    second_array=[]
    files=[f for f in os.listdir(pathOut)if isfile(join(pathOut, f))]
    count=0
    for i in range (len(files)):
        nextFrameString="frame" +str(count+1) + ".jpg"
        if path.exists(pathOut + nextFrameString):
            img2=pathOut + "frame" +str(count+1) + ".jpg" 
            img1=pathOut + "frame" +str(count) + ".jpg"
            diff1 = diff(img2, img1)
            val = diff1*100
            print("file1 :" + img1 + " file2: " + img2 + "diff : " + str(val))
            count = count+1

