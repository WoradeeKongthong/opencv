"""
Morphological คือ process and analysis ด้วย พื้นผิว, ขนาด, รูปร่าง
4 operation/transformation
 - Dilation การขยายภาพ ใช้ขยายให้เห็น noise ชัดขึ้น
 - Erosion การกร่อนภาพ ทำให้เห็น noise น้อยลง แต่วัตถุก็ถูกกร่อนไปด้วย
 - opening การเปิดภาพ ใช้กำจัดวัตถุขนาดเล็ก
 - closing การปิดภาพ ใช้กำจัดช่องโหว่เล็กๆในภาพ และเชื่อมต่อภาพ

ขั้นตอนการทำ image processing ที่นิยม ได้แก่
1. grayscale > thresholding > dilation > erosion
2. grayscale > thresholding > dilation > opening
"""
import cv2
import numpy as np
from stacking_images import stackImages

img = cv2.imread('source/coffee05.jpg',0)

kernel = np.ones((3,3),np.uint8)

imgDilate = cv2.dilate(img, kernel)
imgErode = cv2.erode(img, kernel)
imgOpen = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
imgClose = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

stackImg = stackImages(0.5, [[img, imgDilate, imgErode],[img, imgOpen, imgClose]])
cv2.imshow('img',stackImg)
cv2.waitKey(0)
cv2.destroyAllWindows()