import cv2
import numpy as np

# detect object with TrackBars in HSV mode
def empty(a):
    pass
cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars', 600,200)
cv2.createTrackbar('min Hue', 'Trackbars', 0,255,empty)
cv2.createTrackbar('max Hue', 'Trackbars', 175,255,empty)
cv2.createTrackbar('min Sat', 'Trackbars', 0,255,empty)
cv2.createTrackbar('max Sat', 'Trackbars', 82,255,empty)
cv2.createTrackbar('min Val', 'Trackbars',116,255,empty)
cv2.createTrackbar('max Val', 'Trackbars',227,255,empty)

img = cv2.imread('source/cup.jpg')
(h, w, d) = img.shape
new_w = 400
new_h = int((new_w/w) * h)
dim = (new_w, new_h)
img = cv2.resize(img, dim)

while True:
	
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	h_min = cv2.getTrackbarPos('min Hue', 'Trackbars')
	h_max = cv2.getTrackbarPos('max Hue', 'Trackbars')
	s_min = cv2.getTrackbarPos('min Sat', 'Trackbars')
	s_max = cv2.getTrackbarPos('max Sat', 'Trackbars')
	v_min = cv2.getTrackbarPos('min Val', 'Trackbars')
	v_max = cv2.getTrackbarPos('max Val', 'Trackbars')
	print(h_min, h_max, s_min, s_max, v_min, v_max)
	lower = np.array([h_min, s_min, v_min])
	upper = np.array([h_max, s_max, v_max])
	mask = cv2.inRange(hsv, lower, upper)
	result = cv2.bitwise_and(img, img, mask=mask)

	#cv2.imshow('imgHSV', imgHSV)
	cv2.imshow('img',img)
	cv2.imshow('hsv',hsv)
	cv2.imshow('mask',mask)
	cv2.imshow('result', result)

	if cv2.waitKey(1) & 0xFF == ord('q'):
         break
     
cv2.waitKey(0) #0=never close, 5000=5000ms
cv2.destroyAllWindows()
