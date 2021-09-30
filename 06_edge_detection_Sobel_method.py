"""
Edge Detection ด้วย Sobel Method
   โดยใช้ convolution ในแนวตั้งและแนวนอน
"""

import cv2
import numpy as np

img = cv2.imread("source/cup.jpg",0)
w = img.shape[1]
h = img.shape[0]
img = cv2.resize(img, (int(w/2.5), int(h/2.5)))
sobelx = cv2.Sobel(img, -1, 1, 0)
sobely = cv2.Sobel(img, -1, 0, 1)
sobelxy = cv2.bitwise_or(sobelx, sobely)

stackImg = np.hstack([img, sobelx, sobely, sobelxy])

cv2.imshow('output', stackImg)
cv2.waitKey(0)
cv2.destroyAllWindows()