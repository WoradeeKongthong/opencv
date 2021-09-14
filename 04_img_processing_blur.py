"""
Blur ช่วยลด noise ได้ภาพที่เรียบเนียนกว่า convolution
มี 3 แบบ
 - mean blur
 - median blur
 - gaussian blur
"""
import cv2
import numpy as np
from stacking_images import stackImages

img = cv2.imread('source/coffee05.jpg', 0)

k = 5

imgMeanBlur = cv2.blur(img, (k,k))
imgMedianBlur = cv2.medianBlur(img, k)
imgGaussianBlur = cv2.GaussianBlur(img, (k,k), 0)

stackImg = stackImages(0.75, [[img, imgMeanBlur],[imgMedianBlur, imgGaussianBlur]])
cv2.imshow('output', stackImg)
cv2.waitKey(0)
cv2.destroyAllWindows()