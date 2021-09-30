"""
Edge Detection ด้วย Laplacian Method
   การกรองภาพ ปรับปรุงภาพ และหาขอบในเวลาเดียวกัน
"""

import cv2
import numpy as np

img = cv2.imread("source/cup.jpg",0)
w = img.shape[1]
h = img.shape[0]
img = cv2.resize(img, (int(w/2.5), int(h/2.5)))
laplacian = cv2.Laplacian(img, -1)

stackImg = np.hstack([img, laplacian])

cv2.imshow('output', stackImg)
cv2.waitKey(0)
cv2.destroyAllWindows()