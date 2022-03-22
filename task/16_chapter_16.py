# Saving HD recording of cam streaming

import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

# making a function
def hd_resolution():
    cap.set(3, 1280) # width
    cap.set(4,720) # height
    cap.set(cv.CAP_PROP_FPS, 30)

def sd_resolution():
    cap.set(3, 640) # width
    cap.set(4,480) # height
    cap.set(cv.CAP_PROP_FPS, 30)


def fhd_resolution():
    cap.set(3, 1920) # width
    cap.set(4,1080) # height
    cap.set(cv.CAP_PROP_FPS, 30)


# sd_resolution()
hd_resolution()
# fhd_resolution()

# writing format, codec, video writer object and file output
frame_width= int(cap.get(3))
frame_height = int(cap.get(4))
out= cv.VideoWriter("resources/cam_video.avi", cv.VideoWriter_fourcc("M", "J", "P", "G"),30,(frame_width, frame_height))
while (True):
    (ret, frame) = cap.read()
    #to show in player
    if ret== True:
        out.write(frame)
        cv.imshow('Video', frame)
       # to quit with q-key 
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv.destroyAllWindows()