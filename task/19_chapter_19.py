# coordinates of an image or a video
# bgr color codes from an image

# Step-1 Import libraries

import cv2 as cv 
import numpy as np

# Step-2 Define a function

def find_coord(event, x,y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
    # left mouse click
        print(x,'',y,'')
    # how to define or print on the same image or window
        font=cv.FONT_HERSHEY_PLAIN #making a font style
        cv.putText(img, str(x) + ',' + str(y), (x,y), font, 1.2, (255,0,255), thickness=2)
    # show text on image and image itself
        cv.imshow('image', img)
    # for color finding

    if event == cv.EVENT_RBUTTONDOWN:
        print(x,',',y)

        font = cv.FONT_HERSHEY_SIMPLEX
        b = img[y,x,0] # width height and color channel
        g = img[y,x,1]
        r = img[y,x,2]
        cv.putText(img, str(b) + ',' + str(g) + ',' + str(r), (x,y), font, 1, (255,0,255), 2)
        cv.imshow('image', img)
# Step-3 final function to read and display

if __name__=='__main__':
    # reading an image
    img = cv.imread('resources/warp.png',1)
    img=cv.resize(img, (600,600))
    # display the image
    cv.imshow('image', img)
    #setting call back function
    cv.setMouseCallback('image', find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()