import numpy as np
import cv2

source = cv2.imread('source/legos04.jpg')
target = cv2.imread('source/legos02.jpg')

# resize images
def resize(img, new_w):
	(h, w, d) = img.shape
	new_w = new_w
	new_h = int((new_w/w) * h)
	dim = (new_w, new_h)
	return cv2.resize(img, dim)
source = resize(source, 300)
target = resize(target, 300)

# convert images to L*a*b* mode
source_img = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype('float32')
target_img = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype('float32')

# compute color statistics for both images
def image_stats(img):
	(l, a, b) = cv2.split(img)
	return (l.mean(), l.std(), a.mean(), a.std(), b.mean(), b.std())
lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc = image_stats(source_img)
lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar = image_stats(target_img)

# subtract target means from target image
(l, a, b) = cv2.split(target_img)
l -= lMeanTar
a -= aMeanTar
b -= bMeanTar

# scale by standard deviation ratio
l = l * (lStdTar / lStdSrc)
a = a * (aStdTar / aStdSrc)
b = b * (bStdTar / bStdSrc)

# add source mean
l += lMeanSrc
a += aMeanSrc
b += bMeanSrc

# clip the pixel values to[0, 255]
l = np.clip(l, 0, 255)
a = np.clip(a, 0, 255)
b = np.clip(b, 0, 255)

# merge the channels and convert back to BGR
transfer_img = cv2.merge([l, a, b])
transfer_img = cv2.cvtColor(transfer_img.astype('uint8'), cv2.COLOR_LAB2BGR)

cv2.imshow('source', source)
cv2.imshow('target', target)
cv2.imshow('transfer', transfer_img)
cv2.waitKey(0)
cv2.destroyAllWindows()