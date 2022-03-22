# setting of camera or video

import cv2 as cv
import numpy as np
cap= cv.VideoCapture(0)

cap.set(10,50) #10 is the brightness key and 50% is the brightnessq

cap.set(3,640) #width key is 3 and 640 is the argument
cap.set(4,480) #height key is 4 and 420 is the argument

while (True):
    (ret, frame) = cap.read()
    if ret== True:
        cv.imshow('Video', frame)
       # to quit with q-key 
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
cv.destroyAllWindows()