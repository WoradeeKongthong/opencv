# detect object with TrackBars in HSV mode

import cv2
import numpy as np
import stacking_images

# create empty function
def empty(a):
    pass

# create trackbars for HSV control
cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars', 600,200)
cv2.createTrackbar('min Hue', 'Trackbars', 0,255,empty)
cv2.createTrackbar('max Hue', 'Trackbars', 175,255,empty)
cv2.createTrackbar('min Sat', 'Trackbars', 0,255,empty)
cv2.createTrackbar('max Sat', 'Trackbars', 82,255,empty)
cv2.createTrackbar('min Val', 'Trackbars',116,255,empty)
cv2.createTrackbar('max Val', 'Trackbars',227,255,empty)

# load image
img = cv2.imread('source/cup.jpg')
(h, w, d) = img.shape
new_w = 400
new_h = int((new_w/w) * h)
dim = (new_w, new_h)
img = cv2.resize(img, dim)

# apply trackbar value on image
while True :
    # create hsv mode image for masking
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # get values from trackbars
    h_min = cv2.getTrackbarPos('min Hue', 'Trackbars')
    h_max = cv2.getTrackbarPos('max Hue', 'Trackbars')
    s_min = cv2.getTrackbarPos('min Sat', 'Trackbars')
    s_max = cv2.getTrackbarPos('max Sat', 'Trackbars')
    v_min = cv2.getTrackbarPos('min Val', 'Trackbars')
    v_max = cv2.getTrackbarPos('max Val', 'Trackbars')
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # create mask
    mask = cv2.inRange(hsv, lower, upper)
    # apply mask on image
    result = cv2.bitwise_and(img, img, mask=mask)
    # stack images and display
    stackImg=stacking_images.stackImages(1, ([[img,hsv],[mask,result]]))
    cv2.imshow('output',stackImg)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
 
cv2.waitKey(0) #0=never close, 5000=5000ms
cv2.destroyAllWindows()
