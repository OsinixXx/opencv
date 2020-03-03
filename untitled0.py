#!/usr/bin/python3

################################################################################
# Created on Tue Mar  3 22:20:20 2020
#
# @author: osini
################################################################################


import cv2	as cv


img	= cv.imread("penguin.jpg", cv.IMREAD_GRAYSCALE);
cv.imshow("img", img);

