import cv2
import matplotlib.pyplot as plt
import stacking_images

# load image
img = cv2.imread('source/coffee.jpeg',1)#0=grayscale,1=color,-1=alpha

# explore
print('img type : ', type(img))
img.shape

# print/show 1 image with cv2
cv2.imshow('window name', img)
cv2.waitKey(0) #0=never close, 5000=5000ms
cv2.destroyAllWindows()

# show stacking image with np.hstack (same chanel)
imgStack = np.hstack([img, img]) #array
cv2.imshow('imgstack', imgStack)
cv2.waitKey(0)
cv2.destroyAllWindows()

# show stacking image with defined function (different chanel)
imgGRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgStack = stacking_images.stackImages(1, ([[img,imgGRAY]]))
cv2.imshow('window name', imgStack)
cv2.waitKey(0) #0=never close, 5000=5000ms
cv2.destroyAllWindows()

# print/show images with matplotlib subplot (different chanel)
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(121)
plt.imshow(img)
plt.title("BGR")
plt.subplot(122)
plt.imshow(imgRGB)
plt.title("RGB")
plt.show()

# save image
cv2.imwrite('result/coffee_copy.jpg', img)
