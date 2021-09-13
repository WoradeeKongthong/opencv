import cv2
import numpy as np
import datetime

# create canvas 500*500
img = np.ones((500,500,3), np.uint8)*255
img[:] = [120,0,120]

# line
img = cv2.line(img, (10,10),(200,100), (0,255,255), 10)

# arrowed line
img = cv2.arrowedLine(img, (500,500), (350,350), (0,255,0), 7)

# rectangle
img = cv2.rectangle(img, (100,200),(300,300), (255,255,0), 5)

# filled rectangle
img = cv2.rectangle(img, (0,300),(100,450), (0,0,255), -1)

# circle
img = cv2.circle(img, (400,100), 50, (0,0,0), 3)

# text 
img = cv2.putText(img, "Hello cv2", (200,250),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)
img = cv2.putText(img, str(datetime.datetime.now()), (250,495), cv2.FONT_HERSHEY_PLAIN,1,(0,0,120), 1)

# print image
cv2.imshow('img',img)
cv2.waitKey(0) #0=never close, 5000=5000ms
cv2.destroyAllWindows()
