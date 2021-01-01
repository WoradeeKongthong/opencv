import numpy as np
import cv2

def draw_output(img, cnts):
	for i,cnt in enumerate(cnts):
		cv2.drawContours(img, cnt, -1, (255,0,255), 2)
		m = cv2.moments(cnt)
		cX = int(m['m10'] / m['m00'])
		cY = int(m['m01'] / m['m00'])
		cv2.putText(img, '#'+str(i), (cX-10, cY), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)
	return img

# load image and resize
img = cv2.imread('source/cups.png')
(h, w, d) = img.shape
new_w = 600
new_h = int((new_w/w) * h)
dim = (new_w, new_h)
img = cv2.resize(img, dim)

# image preprocessing
kernel = np.ones((5,5), np.uint8)
img_mod = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_mod = cv2.Canny(img_mod, 150, 200)
img_mod = cv2.dilate(img_mod, kernel, iterations=3)
img_mod = cv2.erode(img_mod, kernel, iterations=3)

# find contours
cnts, _ = cv2.findContours(img_mod.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
unsorted = draw_output(img.copy(), cnts)

# sorting by AREA (small-to-large)
cnts = sorted(cnts, key=cv2.contourArea, reverse=False)
areaSorted = draw_output(img.copy(), cnts)

# sorting by position (left-to-right)
# create bounding boxes (x, y, w, h)
bboxes = [cv2.boundingRect(c) for c in cnts]
(cnts, bboxes) = zip(*sorted(zip(cnts, bboxes), key=lambda b:b[1][0], reverse=False))
positionSorted = draw_output(img.copy(), cnts)

#cv2.imshow('img', img)
#cv2.imshow('mod', img_mod)
cv2.imshow('unsorted', unsorted)
cv2.imshow('Area sorting', areaSorted)
cv2.imshow('Position sorting', positionSorted)
cv2.waitKey(0)
cv2.destroyAllWindows()

#print(bboxes[0])