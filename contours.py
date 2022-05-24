import cv2

original = cv2.imread('./assets/python.png')
img = original.copy()
# cv2.imshow('original', img)

#konwersja do szarosci
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

#wydobycie maski
thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh', thresh)

#detekcja konturów
contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
print(len(contours))

img_cnt = cv2.drawContours(img.copy(), [contours[0]], -1, (0, 255, 0), 2)
# cv2.imshow('contours', img_cnt)

#pole konturów
area = cv2.contourArea(contours[4], True)
print(area)

max_area = 0
for idx, contour in enumerate(contours):
    area = cv2.contourArea(contour, True)
    if max_area < area:
        max_area = area
        idx_flag_area = idx

print(f'max index: {idx_flag_area}, max area: {max_area}')
img_max_contour = cv2.drawContours(img.copy(), [contours[idx_flag_area]], -1, (0, 255, 0), 2)
cv2.imshow('max_contour', img_max_contour)

perimiter = cv2.arcLength(contours[idx_flag_area], True)
print(perimiter)

cv2.waitKey()