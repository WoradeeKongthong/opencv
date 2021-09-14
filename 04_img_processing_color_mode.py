import cv2
from stacking_images import stackImages

# OPTION 1 : SELECT COLOR MODE AS READING
imgColor = cv2.imread('source/coffee.jpeg',1)#0=grayscale,1=color,-1=alpha
imgGray = cv2.imread('source/coffee.jpeg',0)#0=grayscale,1=color,-1=alpha

stackImg = stackImages(1, [imgColor,imgGray])
cv2.imshow('OPTION 1 OUTPUT', stackImg)
cv2.waitKey(0) #0=never close, 5000=5000ms
cv2.destroyAllWindows()

# OPTION 2 : CONVERT COLOR MODE AFTER READING
img = cv2.imread('source/coffee.jpeg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

stackImg = stackImages(1, [img,imgGray])
cv2.imshow('OPTION 2 OUTPUT', stackImg)
cv2.waitKey(0) #0=never close, 5000=5000ms
cv2.destroyAllWindows()
