import cv2

frameWidth = 640
frameHeight = 480

# read webcam
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth) #set width
cap.set(4, frameHeight) #set height
cap.set(10,120) #set brightness original=100

# display webcam
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# write video
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
result = cv2.VideoWriter("result/webcam.avi", fourcc, 20.0, (640,480))

while cap.isOpened():
    check, frame = cap.read()
    if check == True:
        frame = cv2.resize(frame, (frameWidth, frameHeight))
        result.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
result.release()
cv2.destroyAllWindows()
