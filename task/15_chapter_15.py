# resolution of cam

import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

# Resolution HD(1280,720)
cap.set(3, 1280) # width
cap.set(4,720) # height

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


sd_resolution()
# hd_resolution()
# fhd_resolution()

while(True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('camera', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()