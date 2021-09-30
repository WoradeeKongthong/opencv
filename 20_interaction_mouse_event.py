"""
mouse event ใช้ทำอะไรได้บ้าง
 - บอกพิกัด x, y
 - ระบุค่าสีที่พิกเซลนั้นๆ
"""
import cv2

img = cv2.imread('source/cards.jpg')
w,h,d = img.shape
new_w = 700
img = cv2.resize(img, (new_w, int(new_w/w * h)))

def callbackFn(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = str(x) + ',' + str(y)
        cv2.putText(img, text, (x,y), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,255), 2)
        cv2.imshow('output', img)

cv2.imshow('output',img)
cv2.setMouseCallback('output', callbackFn)
cv2.waitKey(0)
cv2.destroyAllWindows()