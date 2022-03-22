## Reading an image and displaying it

# import library
import cv2 as cv

img = cv.imread('resources/ehtisham.png')

cv.imshow('Pehli Image', img)
cv.waitKey(0)