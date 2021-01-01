import numpy as np
import cv2

img = cv2.imread('source/cup.jpg')
(h, w, d) = img.shape
new_w = 400
new_h = int((new_w/w) * h)
dim = (new_w, new_h)
img = cv2.resize(img, dim)

output = img.copy()

# image preprocessing
img_mod = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_mod = cv2.GaussianBlur(img_mod, (5,5), 0)
img_mod = cv2.threshold(img_mod, 160, 255, cv2.THRESH_BINARY)[1]
img_mod = cv2.dilate(img_mod, None, iterations=10)
img_mod = cv2.erode(img_mod, None, iterations=10)

# find contours and draw the largest one
contours, hierarchy = cv2.findContours(img_mod.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
c = max(contours, key=cv2.contourArea)
cv2.drawContours(output, c, -1, (255,0,255), 2)

# CENTER from IMAGE MOMENTS
m = cv2.moments(c)
cX = int(m['m10'] / m['m00'])
cY = int(m['m01'] / m['m00'])
cv2.circle(output, (cX, cY), 5,(255,0,255), -1)
cv2.putText(output, 'center', (cX-25, cY-15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255), 2)

# find extreme points along the contour
extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

# draw extreme points
cv2.circle(output, extLeft, 5, (0, 255, 0), -1)
cv2.circle(output, extRight, 5, (0, 0, 255), -1)
cv2.circle(output, extTop, 5, (255, 0, 0), -1)
cv2.circle(output, extBot, 5, (0, 255, 255), -1)

cv2.imshow('preprocessed img', img_mod)
cv2.imshow('output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()