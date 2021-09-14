import cv2

# load image
img = cv2.imread('source/coffee.jpeg')
print(img.shape)

#====================================================
# resize without aspect ratio
w = 300
h = 500
imgResized = cv2.resize(img, (w, h))

cv2.imshow('resize', imgResized)
cv2.waitKey(0)
cv2.destroyAllWindows()

#====================================================
# resize with keep aspect ratio
old_w = img.shape[1]
old_h = img.shape[0]
ratio = old_w / old_h

# ratio = w/h
w = 300
h = int(w / ratio)
imgResized = cv2.resize(img, (w,h))

cv2.imshow('resize with aspect ratio', imgResized)
cv2.waitKey(0)
cv2.destroyAllWindows()

#====================================================