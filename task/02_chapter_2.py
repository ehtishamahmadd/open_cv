## Resizing an image and displaying it

# import library
import cv2 as cv

img = cv.imread('resources/ehtisham.png')
img1 = cv.resize(img,(500,600))

cv.imshow('Pehli Image', img)
cv.imshow('Dosri Image', img1 )
cv.waitKey(0)
cv.destroyAllWindows()