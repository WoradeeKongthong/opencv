import cv2
import numpy as np

# create empty function
def empty(a):
    pass

# create trackbar
cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars', 600,200)
cv2.createTrackbar('min threshold', 'Trackbars', 0,255,empty)
cv2.createTrackbar('max threshold', 'Trackbars', 0,255,empty)

# load image
img = cv2.imread('source/cup.jpg')
(h, w, d) = img.shape
new_w = 400
new_h = int((new_w/w) * h)
dim = (new_w, new_h)
img = cv2.resize(img, dim)

# create grayscale img
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while True:
    # apply value from trackbar on grayscale image
    thresh_min = cv2.getTrackbarPos('min threshold', 'Trackbars')
    thresh_max = cv2.getTrackbarPos('max threshold', 'Trackbars')
    thresh = cv2.threshold(gray, thresh_min, thresh_max, cv2.THRESH_BINARY)[1]

    # show result
    imgStack = np.hstack([gray, thresh])
    cv2.imshow('thresholding', imgStack)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
     
cv2.waitKey(0) #0=never close, 5000=5000ms
cv2.destroyAllWindows()
