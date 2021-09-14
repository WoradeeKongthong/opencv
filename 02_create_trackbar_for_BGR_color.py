import cv2
import numpy as np

# create empty function
def empty(a):
    pass

# create trackbar
cv2.namedWindow('Trackbars')
# cv2.resizeWindow('Trackbars', 600,200)
cv2.createTrackbar('blue', 'Trackbars', 0,255,empty)
cv2.createTrackbar('green', 'Trackbars', 0,255,empty)
cv2.createTrackbar('red', 'Trackbars', 0,255,empty)

# create canvas
img = np.ones((500,500,3), np.uint8)*255

while True:
    # apply value from trackbar on grayscale image
    blue = cv2.getTrackbarPos('blue', 'Trackbars')
    green = cv2.getTrackbarPos('green', 'Trackbars')
    red = cv2.getTrackbarPos('red', 'Trackbars')
    # draw filled circle
    img = cv2.circle(img, (250,250), 150, (blue,green,red), -1)

    # show result
    cv2.imshow('result', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
     
cv2.waitKey(0) #0=never close, 5000=5000ms
cv2.destroyAllWindows()
