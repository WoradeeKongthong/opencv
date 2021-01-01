import cv2
import numpy as np

img = cv2.imread('source/cup.jpg')
(h, w, d) = img.shape
new_w = 400
new_h = int((new_w/w) * h)
dim = (new_w, new_h)
img = cv2.resize(img, dim)

# image processing
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)[1]
mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=10)
mask = cv2.erode(mask, None, iterations=10)
result = cv2.bitwise_and(img, img, mask=mask)

#cv2.imshow('img', img)
#cv2.imshow('gray', gray)
cv2.imshow('thresh', thresh)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()