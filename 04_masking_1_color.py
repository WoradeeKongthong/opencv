import numpy as np
import cv2

img = cv2.imread('source/cups.png')
(h, w, d) = img.shape
new_w = 250
new_h = int((new_w/w) * h)
dim = (new_w, new_h)
img = cv2.resize(img, dim)

# define color boundaries
lower = np.array([150, 80, 0], np.uint8)
upper = np.array([255,150,10], np.uint8)

# masking
mask = cv2.inRange(img, lower, upper)

# combine mask with image
output = cv2.bitwise_and(img, img, mask=mask)

# show result
import matplotlib.pyplot as plt
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
maskRGB = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
outputRGB = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
plt.subplot(1,3,1)
plt.imshow(imgRGB)
plt.title("img")
plt.subplot(1,3,2)
plt.imshow(maskRGB)
plt.title("mask")
plt.subplot(1,3,3)
plt.imshow(outputRGB)
plt.title("output")
plt.show()

