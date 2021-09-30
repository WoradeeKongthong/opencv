"""
Edge Detection ด้วย Canny Method
   การหาขอบภาพที่ได้รับความนิยม 
   ใช้การเปรียบเทียบ threshold 2 ค่าเพื่อหาพื้นที่ที่
   มีความเข้มต่างกัน
   (มักเกิด error ถ้ามี noise เยอะเกินไป)
"""

import cv2
import numpy as np

img = cv2.imread("source/cup.jpg",0)
w = img.shape[1]
h = img.shape[0]
img = cv2.resize(img, (int(w/2.5), int(h/2.5)))
canny = cv2.Canny(img, 50, 250)

stackImg = np.hstack([img, canny])

cv2.imshow('output', stackImg)
cv2.waitKey(0)
cv2.destroyAllWindows()