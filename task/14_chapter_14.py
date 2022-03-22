# how to draw lines, and shapes in python

import cv2 as cv
import numpy as np

# draw a canvas 0 is for black
img = np.zeros((600,600)) #black (600 rows and 600 columns)
img1 = np.ones((600,600)) #ones for white

# print size
# print('The size of our canvas is:', img.shape)

# adding colors to the canvas
colored_img = np.zeros((600,600,3), np.uint8) # color channel addition

colored_img[:] = 255,0,255 # color key complete image

colored_img[150:230, 100:500] = 255,168,10 # color key partial(part of) image

# adding a line
cv.line(colored_img, (0,0), (colored_img.shape[0] , colored_img.shape[1]),(255,0,0),3) #complete line
cv.line(colored_img, (100,100),(300,300),(255,255,50),3) #part line

# adding rectangles
cv.rectangle(colored_img,(50,100),(300,400),(255,255,255),3) #giving thickness to a rectangle
cv.rectangle(colored_img,(50,100),(300,400),(255,255,255), cv.FILLED) #filling full rectangle

# adding a circle
cv.circle(colored_img,(400,300),50,(255,100,0), cv.FILLED)


# adding text
cv.putText(colored_img,'Python ka chilla on',(50,500), cv.FONT_HERSHEY_DUPLEX,1, (255,255,0),1)

cv.putText(colored_img,'codanics Youtube channel',(50,525), cv.FONT_HERSHEY_DUPLEX,1, (255,255,0),1)

# cv.imshow('Black', img)
# cv.imshow('White', img1)
cv.imshow('colored',colored_img)
cv.waitKey(0)
cv.destroyAllWindows()