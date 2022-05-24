import cv2

def get_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'{x} {y}')

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (0, 0, 255), 2)


img = cv2.imread('./assets/tesla.jpg')

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) == 27:
        break

