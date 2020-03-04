#!/usr/bin/python3
import cv2
import numpy as np

img = cv2.imread("Examm.jpeg",1)
while(1):
#transformation
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    green_low = np.array([80,230,50])
    green_high = np.array([160,255,90])

#Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, green_low, green_high)

#Bitwise-AND mask and original image
    res = cv2.bitwise_and(img, img, mask= mask)

#show images
    cv2.imshow('img', img)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()