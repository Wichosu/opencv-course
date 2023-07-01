import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/cat.jpeg')
cv.imshow('Cat', img)

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv.waitKey(0)