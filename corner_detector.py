import cv2
import numpy as np
import imutils

img = cv2.imread('./assets/cube.jpg')
img = imutils.resize(img, height=600)
# cv2.imshow('img', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imshow('img', img)
cv2.waitKey()

