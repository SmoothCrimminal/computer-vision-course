import cv2

img = cv2.imread('./assets/grey.png', 0)
print(img)
cv2.imshow('img', img)

thresh_binary = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('thresh_binary', thresh_binary)

cv2.waitKey()