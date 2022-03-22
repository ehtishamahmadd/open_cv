# how to capture a webcam inside python

# Step-1 Import Libraries
import cv2 as cv
import numpy as np

#Step-2 Read the frames from camera
cap= cv.VideoCapture(0) #webcame number

# read until the end
#Step-3 Display frames by frames
while(cap.isOpened()):
    #capture frame by frame
    ret, frame = cap.read()
    if ret==True:
        # to desplay frame
        cv.imshow('Frame', frame)
         # to quit with q-key 
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
#Step-4 Release and close windows easily
cap.release()
cv.destroyAllWindows()