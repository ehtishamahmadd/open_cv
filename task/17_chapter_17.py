# Joining two images

import cv2 as cv 
import numpy as np

img1 = cv.imread('resources/ehtisham.png')
img2 = cv.imread('resources/img.png')
img1 = cv.resize(img1,(300,400))
img2 = cv.resize(img2,(300,400))
# stacking same image

#1- Horizontal stack

# hor_img = np.hstack((img1,img1))

# #2- vertical stack
# ver_img = np.vstack((img,img))

# cv.imshow('Horizontal', hor_img)
# cv.imshow('Vertical', ver_img)



# you can only stack images with same shaped(width, height, color channel) (600,500,3)
# assignmnet: define a function to stack mutliple images of different sizes and tunes
# define function for stacking
# same no of color channels


def vconcat_resize_min(im_list, interpolation=cv.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv.vconcat(im_list_resize)

def hconcat_resize_min(im_list, interpolation=cv.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv.hconcat(im_list_resize)

def concat_tile_resize(im_list_2d, interpolation=cv.INTER_CUBIC):
    im_list_v = [hconcat_resize_min(im_list_h, interpolation=cv.INTER_CUBIC) for im_list_h in im_list_2d]
    return vconcat_resize_min(im_list_v, interpolation=cv.INTER_CUBIC)

im_tile_resize = concat_tile_resize([[img1, img2],
                                     [img1, img2, img1, img2, img1],
                                     [img1, img2, img1]])


cv.imshow('Stacking', im_tile_resize )

cv.waitKey(0)
cv.destroyAllWindows()