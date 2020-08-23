import sys
import argparse

import cv2
print(cv2.__version__)


def extractImages(pathIn, pathOut):
    pathIn = 'C:\\Users\\kunal\\Desktop\\Trial\\Video\\1999187004.mp4'
    pathOut = 'C:\\Users\\kunal\\Desktop\\Trial\\Frames'
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success, image = vidcap.read()
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count*1000))    # added this line
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        cv2.imwrite(pathOut + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
        count = count + 1
    while not success:
        print('nothing to get frame from')
        exit()


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut)
