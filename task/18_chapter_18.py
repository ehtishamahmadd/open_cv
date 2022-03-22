# how to change the prospective of an image(alligning the image)

from email.base64mime import header_encode
import cv2 as cv 
import numpy as np

img= cv.imread('resources/warp.png')
img = cv.resize(img,(600,600))
print(img.shape)

# defining points

point1= np.float32([[190,52],[78,408],[528,172],[421,531]])

width = 600
height = 600
width,height = 600,600

point2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# # reading document points(corner) in matrix form

matrix= cv.getPerspectiveTransform(point1, point2)
out_img = cv.warpPerspective(img, matrix, (width, height))
out_img= cv.resize(out_img,(400,400))
cv.imwrite('resources/warp_prespective.png', out_img)
cv.imshow('Original', img)
cv.imshow('Transformed', out_img)

cv.waitKey(0)
cv.destroyAllWindows()