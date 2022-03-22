# how to detect specific colors inside python

import cv2 as cv 
import numpy as np

# img =cv.imread('resources/ehtisham.png')
# img = cv.resize(img, (500,600))

# # converting in hsv(hue,saturation,vaue)
# hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# sliders

def slider():
    pass
path = 'resources/ehtisham.png'

cv.namedWindow("bars")
cv.resizeWindow('bars', 800,300)
cv.createTrackbar('Hue Min', 'bars', 0,179,slider)
cv.createTrackbar('Hue Max', 'bars', 179,179,slider)
cv.createTrackbar('Sat Min', 'bars', 0,255,slider)
cv.createTrackbar('Sat Max', 'bars', 255,255,slider)
cv.createTrackbar('Val Min', 'bars', 0,255,slider)
cv.createTrackbar('Val Max', 'bars', 255,255,slider)

img = cv.imread(path)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# hue_min = cv.getTrackbarPos("Hue Min", "bars")
# print(hue_min)

while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos("Hue Min", "bars")
    hue_max = cv.getTrackbarPos("Hue Max", "bars")
    sat_min = cv.getTrackbarPos("Sat Min", "bars")
    sat_max = cv.getTrackbarPos("Sat Max", "bars")
    val_min = cv.getTrackbarPos("Val Min", "bars")
    val_max = cv.getTrackbarPos("Val Max", "bars")
    print(hue_min,hue_max, sat_min,sat_max,val_min,val_max)


    #to see these changes inside an image
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max,sat_max,val_max])
    mask_img = cv.inRange(hsv_img, lower, upper)
    out_img = cv.bitwise_and(img,img, mask=mask_img)

    # cv.imshow('Original', img)
    # cv.imshow('HSV', hsv_img)
    cv.imshow('Mask', mask_img)
    cv.imshow('Final Output', out_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
