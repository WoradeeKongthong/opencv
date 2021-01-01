import cv2
import numpy as np

img = cv2.imread('source/geometry.png')
(h, w, d) = img.shape
new_w = 400
new_h = int((new_w/w) * h)
dim = (new_w, new_h)
img = cv2.resize(img, dim)

output = img.copy()


# image processing
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (7,7), 1)
img = cv2.Canny(img, 50, 50)

# find contours
contours, hierarchy = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for cnt in contours:
	#print(cnt)
	
	# PERIMETER
	peri = cv2.arcLength(cnt, True)
	#print(peri)
	
	# CORNERS
	approx = cv2.approxPolyDP(cnt, 0.04*peri, True)
	#for i in approx:
	#	cv2.circle(output, (i[0][0], i[0][1]), 5, (255, 0, 0), -1)

	# BOUNDING BOX AROUND CORNERS
	x, y, w, h = cv2.boundingRect(approx)
	cv2.rectangle(output, (x,y), (x+w, y+h), (0,255,0), 2)

	# CENTER from IMAGE MOMENTS
	#m = cv2.moments(cnt)
	#cX = int(m['m10'] / m['m00'])
	#cY = int(m['m01'] / m['m00'])
	#cv2.circle(output, (cX, cY), 5,(255,255,255), -1)

	# AREA
	#area = cv2.contourArea(cnt)
	#cv2.putText(output, str(area), (x+w//2 - 15, y+h//2), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)
 
	# GEOMETRIC SHAPE (Tri/Sqr/Rec/Cir)
	if len(approx) == 3 :
		objType = 'Tri'
	elif len(approx) == 4:
		ratio = w/float(h)
		if ratio > 0.95 and ratio < 1.05:
			objType = 'Sqr'
		else: 
			objType = 'Rec'
	else:
		objType = 'Cir'
	cv2.putText(output, objType, (x+w//2 - 15, y+h//2+5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)

	cv2.drawContours(output, cnt, -1, (255,0,255), 2)


#cv2.imshow('img', img)
cv2.imshow('contour', output)
cv2.waitKey(0)
cv2.destroyAllWindows()