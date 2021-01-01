import numpy as np
import cv2

img = cv2.imread('source/cups.png')
(h, w, d) = img.shape
new_w = 250
new_h = int((new_w/w) * h)
dim = (new_w, new_h)
img = cv2.resize(img, dim)

# define list of color boundaries
boundaries = [
([150, 80, 0], [255,150,10]),
([70,0,120],[150,100,250]),
([0,70,200], [10,170,255]),
([20,100,0], [100,255,110])
]

outputs = []
for i, (lower, upper) in enumerate(boundaries):
	lower = np.array(lower, dtype='uint8')
	upper = np.array(upper, dtype='uint8')
	mask = cv2.inRange(img, lower, upper)
	output = cv2.bitwise_and(img, img, mask=mask)
	outputs.append(output)

imgStack = np.hstack([output for output in outputs])
cv2.imshow('imgstack', imgStack)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()