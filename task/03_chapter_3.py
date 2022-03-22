## grayscale conversion

# import library
import cv2 as cv

img = cv.imread('resources/IMG_146111.jpg')
img = cv.resize(img,(500,600))

#conversion
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#display code
cv.imshow('Pehli Image', img)
cv.imshow('Gray Image', gray_img )

#delay code
cv.waitKey(0)
cv.destroyAllWindows()