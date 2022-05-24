import cv2

print(cv2.__version__)

#load image
image = cv2.imread('./assets/bear.jpg')
cv2.imshow('bear', image)
cv2.waitKey()

#rysowanie
height, width = image.shape[:2]
print(f'Wysokość: {height}')
print(f'Szerokość: {width}')

cv2.line(image, (0, 0), (width, height), (0, 0, 255), 5)
cv2.imshow('img', image)
cv2.waitKey()