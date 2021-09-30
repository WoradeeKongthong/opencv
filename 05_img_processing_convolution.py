"""
Convolution คือ การกรองข้อมูลจากภาพ 
สามารถใช้ convolution ลด noise ได้ คล้ายการ Blur
"""
import cv2
import numpy as np

img = cv2.imread('source/coffee05.jpg', 0)

kernel = np.ones((3,3), np.float32) / 10

imgConv = cv2.filter2D(img, -1, kernel)

stackImg = np.hstack([img, imgConv])
cv2.imshow('output', stackImg)
cv2.waitKey(0)
cv2.destroyAllWindows()