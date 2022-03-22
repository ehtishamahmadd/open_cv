# basic function and manipulation in open cv

import cv2 as cv
import numpy as np
img=cv.imread('resources/ehtisham.png')
img=cv.resize(img,(500,600))
# resize
resized_img= cv.resize(img,(350,250))

# gray image
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# blurred image
blurr_img=cv.GaussianBlur(img, (7,7),0) # 7,7 is matrix for blur intensity and it should always be an odd value
# 0 is the sigmax that controls the variation around the mean value(filters)

# black and white image

(thresh, binary)= cv.threshold(gray_img, 127,255, cv.THRESH_BINARY)

# edge detection

edge_img=cv.Canny(img,53,53) # we can trace image on color detection method

# thickness(dilation) of lines
mat_kernel=np.ones((3,3), np.uint8) # matrix for thickness
dilated_img= cv.dilate(edge_img,(mat_kernel),iterations=1)


# erosion(thinner) outline (opposite of thickness)
ero_img = cv.erode(dilated_img,mat_kernel,iterations=1)

#cropping an image(we will use numpy not open cv because it will give us shape of our original image)
print('The size of our image is:', img.shape)
cropped_img = img [0:300, 150:350]

cv.imshow('original', img)
cv.imshow('resized', resized_img)
cv.imshow('gray', gray_img)
cv.imshow('blurr', blurr_img)
cv.imshow('b&w', binary)
cv.imshow('edge', edge_img)
cv.imshow('dilated', dilated_img)
cv.imshow('erosion', ero_img)
# cv.imshow('cropped', cropped_img)

cv.waitKey(0)
cv.destroyAllWindows()