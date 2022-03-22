# face detecttion in images

import cv2 as cv

# making a cascade/window

face_cascade = cv.CascadeClassifier('resources/haarcascade_frontalface_default.xml')

img = cv.imread('resources/faces.png')
img = cv.resize(img,(600,600))
print(img.shape)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)

# draw a rectangle

for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

cv.imshow('image', img)
cv.imwrite('resources/faces.png', img)
cv.waitKey(0)
cv.destroyAllWindows