# masking with threshold on grayscale image then apply to colored image

import cv2
import numpy as np

# load image
img = cv2.imread('source/cup.jpg')
(h, w, d) = img.shape
new_w = 400
new_h = int((new_w/w) * h)
dim = (new_w, new_h)
img = cv2.resize(img, dim)

# create grayscale img
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# create threshold
thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)[1]

# dilate
dilate = cv2.dilate(thresh, None, iterations=10)

# erode 
erode = cv2.erode(dilate, None, iterations=10)

# get mask
mask = erode.copy()

# apply mask on color image
result = cv2.bitwise_and(img, img, mask=mask)

# show results
import matplotlib.pyplot as plt
outputs = [img, gray, thresh, dilate, erode, mask, result]
names = ['img','gray','thresh','dilate','erode','mask','result']
for i, output in enumerate(outputs):
    output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    plt.subplot(3,3,i+1)
    plt.imshow(output)
    plt.title(names[i])
plt.show()