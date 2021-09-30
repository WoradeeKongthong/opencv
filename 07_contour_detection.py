"""
Contour Detection 
   on binary image (image from thresholding)
"""

import cv2
import numpy as np
import stacking_images

img = cv2.imread("source/cup.jpg")
w = img.shape[1]
h = img.shape[0]
img = cv2.resize(img, (int(w/2.5), int(h/2.5)))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# get binary image
thresh, result = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)

# ใช้ morphological (closing) ปิดช่องว่างภายในภาพ
kernel = np.ones((5,5),np.uint8)
result2 = cv2.morphologyEx(result, cv2.MORPH_CLOSE, kernel)

# find contours
contours, hierarchy = cv2.findContours(result2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# จำนวนเส้น contour
len(contours)

# Draw contours on image 
# index 0 to len(contours)-1
# index = -1 : plot all contours
cv2.drawContours(img, contours, 0, (0,0,255), 2)

stackImg = stacking_images.stackImages(1, ([[img,gray],[result,result2]]))

cv2.imshow('output', stackImg)
cv2.waitKey(0)
cv2.destroyAllWindows()