import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpeg')

cv.imshow('Boston', img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimesions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimesions)

#-x ---> Left
#-y ---> Up
# x ---> Right
# y ---> Down

translate = translate(img, -100, 100)
cv.imshow('Translated', translate)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -90)
cv.imshow('Rotated_Rotated', rotated_rotated)

#Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Fliping 
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

#Cropping
cropped = img[100:500, 10:40]
cv.imshow('Cropped', cropped)

cv.waitKey(0)