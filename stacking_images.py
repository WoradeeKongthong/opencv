import cv2
import numpy as np

# image stack function from https://www.murtazahassan.com/
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

# img1 = cv2.imread('legos01.jpg')
# img2 = cv2.imread('legos02.jpg')
# img3 = cv2.imread('legos03.jpg')
# img4 = cv2.imread('legos04.jpg')

# imgStack = stackImages(0.1, ([img1, img2],[img3, img4]))
# cv2.imshow('image stack', imgStack)
# cv2.waitKey(0)

# # normal stack
# def resize(img, new_w, new_h):
#     (h, w, d) = img.shape
#     dim = (new_w, new_h)
#     return cv2.resize(img, dim)

# img1 = resize(img1, 250,300)
# img2 = resize(img2, 250,300)
# img3 = resize(img3, 250,300)
# img4 = resize(img4, 250,300)
# imgHor = np.hstack((img1, img2, img3, img4))
# cv2.imshow('horizontal stack', imgHor)
# cv2.waitKey(0)