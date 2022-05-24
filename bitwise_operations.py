import cv2
import imutils

img = cv2.imread('./assets/view.jpg')
logo = cv2.imread('./assets/python.png')
logo = imutils.resize(logo, height=150)

#wycięcie obszaru roi
rows, cols, channels = logo.shape
roi = img[:rows, :cols]
# cv2.imshow('roi', roi)
# cv2.waitKey()

gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

mask = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)[1]
# cv2.imshow('mask', mask)
# cv2.waitKey()

mask_inv = cv2.bitwise_not(mask)
# cv2.imshow('mask_inv', mask_inv)
# cv2.waitKey()

img_background = cv2.bitwise_and(roi, roi, mask=mask)
logo_foreground = cv2.bitwise_and(logo, logo, mask=mask_inv)
# cv2.imshow('img_bg', img_background)
# cv2.imshow('img_fg', logo_foreground)
# cv2.waitKey()

dst = cv2.add(img_background, logo_foreground)
img[:rows, :cols] = dst
cv2.imshow('out', img)
cv2.waitKey()