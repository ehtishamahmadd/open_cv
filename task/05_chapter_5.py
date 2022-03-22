# image saving and writing images
import cv2 as cv
from cv2 import imwrite
img = cv.imread('resources/image.png')
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary)= cv.threshold(gray, 127,255, cv.THRESH_BINARY)
binary= cv.resize(binary,(400,500))
imwrite('resources/Image_gray.png',gray)
imwrite('resources/image_bw.png',binary)

# cv.waitKey(0)
# cv.destroyAllWindows()