import cv2
import numpy as np

img = cv2.imread('./assets/checkbox.png')

img = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=(255, 255, 255))
# cv2.imshow('img', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow('blurred', blurred)

thresh = cv2.threshold(blurred, 75, 200, cv2.THRESH_BINARY)[1]
cv2.imshow('thresh', thresh)

contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
print(len(contours))

img_cnt = cv2.drawContours(img.copy(), [contours[0]], -1, (0, 255, 0), 2)
cv2.imshow('img', img_cnt)

# wyszukanie konturu z zaznaczonym checkboxem
checked_idx = None
total = 0

for idx in [1, 2]:
    # generowanie maski
    mask = np.zeros(gray.shape, 'uint8')
    cv2.drawContours(mask, [contours[idx]], -1, 255, -1)

    mask_inv = cv2.bitwise_not(mask)
    answer = cv2.add(gray, mask_inv)
    answer_inv = cv2.bitwise_not(answer)
    cnt = cv2.countNonZero(answer_inv)

    if cnt > total:
        checked_idx = idx
print(checked_idx)

img = cv2.drawContours(img, [contours[checked_idx]], -1, (0, 255, 0), 2)
cv2.imshow('checked_contour', img)


cv2.waitKey()