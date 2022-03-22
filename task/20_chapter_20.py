# split your video into frames or image sequence

import cv2 as cv

cap = cv.VideoCapture('resources/cam_video.avi')

frameNr = 0 #frame number object

while(True):
    success, frame = cap.read()
    if success:
        cv.imwrite(f'resources/frames/frames_{frameNr}.jpg', frame)
    else:
        break
    frameNr = frameNr+2
cap.release()