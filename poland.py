import cv2

poland_img = cv2.imread('./assets/poland.png')
cv2.imshow('img', poland_img)

img = cv2.copyMakeBorder(poland_img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=(255, 255, 255))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)[1]

contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
print(len(contours))

img = cv2.drawContours(img, [contours[0]], -1, (0, 255, 0), 2)
cv2.imshow('contours', img)

# punkty ekstremalne
contour = contours[0]
leftmost = contour[contour[:, :, 0].argmin()][0]
rightmost = contour[contour[:, :, 0].argmax()][0]
topmost = contour[contour[:, :, 1].argmin()][0]
bottommost = contour[contour[:, :, 1].argmax()][0]

for point in [leftmost, rightmost, topmost, bottommost]:
    cv2.circle(img, tuple(point), 10, (0, 0, 255), -1)

cv2.imshow('extreme points', img)

cv2.waitKey()
