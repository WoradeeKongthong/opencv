import cv2
import numpy as np

# read an image
img = cv2.imread('source/coffee02.jpg')

# resize the image with aspect ratio
(h, w, d) = img.shape
print('width={}, height={}, depth={}'.format(w, h, d))
new_w = 300
new_h = int((new_w/w) * h)
dim = (new_w, new_h)
img = cv2.resize(img, dim)

# display the image
cv2.imshow('img', img)

# print a pixel value at [100,50]
(B, G, R) = img[100, 50]
print('R={}, G={}, B={}'.format(R, G, B))

# ROI : region of interest (crop)
roi = img[168:285, 59:214]
cv2.imshow('roi', roi)

# rotating the image for 45 degree
(h, w, d) = img.shape
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0) #+for counterclockwise, -for clockwise
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow('rotation', rotated)

# rotating without clipping for 45 degree
(h, w) = img.shape[:2]
(cX, cY) = (w//2, h//2)
M = cv2.getRotationMatrix2D((cX, cY), -45, 1.0)
cos = np.abs(M[0,0])
sin = np.abs(M[0,1])
new_w = int((h*sin) + (w*cos))
new_h = int((h*cos) + (w*sin))
M[0,2] += (new_w/2) - cX
M[1,2] += (new_h/2) -cY
rotate_bound = cv2.warpAffine(img, M, (new_w, new_h))
cv2.imshow('rotate_bound', rotate_bound)

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# thresholding
# if object is brighter use cv2.THRESH_BINARY
# if background is brighter use cv2.THRESH_BINARY_INV
thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('thresh', thresh)

# smoothing an image
blurred = cv2.GaussianBlur(img, (11,11), 0)
cv2.imshow('blurred', blurred)

# edge detection
canny = cv2.Canny(img, 150, 200)
cv2.imshow('canny', canny)

# dilation
kernel = np.ones((5,5), np.uint8)
dilate = cv2.dilate(canny, kernel, iterations=1)
cv2.imshow('dilate', dilate)

# erosion
kernel = np.ones((5,5), np.uint8)
eroded = cv2.erode(dilate, kernel, iterations=1)
cv2.imshow('eroded', eroded)

# draw rectangle (x1,y1),(x2,y2)
output1 = img.copy()
cv2.rectangle(output1, (59, 168), (214, 285), (0, 0, 255), 2)
cv2.imshow('rectangle', output1)

# draw solid circle : thickness = -1 is for solid
output2 = img.copy()
cv2.circle(output2, (50, 50), 20, (255, 0, 0), -1)
cv2.imshow('circle', output2)

# draw a line
output3 = img.copy()
cv2.line(output3, (60, 20), (100, 120), (0, 0, 255), 5)
cv2.imshow('line', output3)

# put text in the image
output4 = img.copy()
cv2.putText(output4, 'Coffee', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 
	0.7, (0, 255, 0), 2)
cv2.imshow('text', output4)

cv2.waitKey(0)
cv2.destroyAllWindows()

# warp perspective
# from original
#    top-left : (0, 81)
#    top-right : (77, 56)
#    bottom-left : (39, 196)
#    bottom-right : (118, 167)
# to 
#    top-left : (0, 0)
#    top-right : (width, 0)
#    bottom-left : (0, height)
#    bottom-right : (width, height)

cards = cv2.imread('source/cards.jpg')
(h, w, d) = cards.shape
new_w = 300
new_h = int((300.0/w) * h)
dim = (new_w, new_h)
cards = cv2.resize(cards, dim)
cv2.imshow('img', cards)

width, height = 250, 350 #of output img
pts1 = np.float32([[0,81],[77,56],
					[39,196],[118,167]])

pts2 = np.float32([[0,0],[width,0],
					[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(cards, matrix, (width, height))
cv2.imshow('output', output)

cv2.waitKey(0)
cv2.destroyAllWindows()