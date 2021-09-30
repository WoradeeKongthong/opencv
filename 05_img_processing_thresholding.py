import cv2
import numpy as np
from stacking_images import stackImages

# load image as grayscale
img = cv2.imread('source/cup.jpg',0)
(h, w) = img.shape
new_w = 400
new_h = int((new_w/w) * h)
dim = (new_w, new_h)
img = cv2.resize(img, dim)

#=================================================================
# thresholding
threshBinary = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)[1]
threshBinaryInv = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY_INV)[1]
threshTrunc = cv2.threshold(img, 160, 255, cv2.THRESH_TRUNC)[1]
threshToZero = cv2.threshold(img, 160, 255, cv2.THRESH_TOZERO)[1]
threshToZeroInv = cv2.threshold(img, 160, 255, cv2.THRESH_TOZERO_INV)[1]

# display result
stackImg = stackImages(0.75,[[img, threshBinary, threshBinaryInv],[threshTrunc, threshToZero,threshToZeroInv]])
cv2.imshow('thresholding',stackImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#=================================================================
# Adaptive thresholding : if an image has different lighting conditions in different areas
# blockSize determines the size of the neighbourhood area
# C is a constant that is subtracted from the mean or weighted sum of the neighbourhood pixels
adapThresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)

cv2.imshow('thresholding',adapThresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
#=================================================================