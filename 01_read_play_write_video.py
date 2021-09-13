import cv2

frameWidth = 700
frameHeight = 480

# read video
cap = cv2.VideoCapture('source/livingroom_tour.mp4')

# show video
while cap.isOpened():
    success, img = cap.read()
    if success :
        img = cv2.resize(img, (frameWidth, frameHeight))
        cv2.imshow("Result", img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break
    else :
        break
cap.release()
cv2.destroyAllWindows()

# write video
cap = cv2.VideoCapture('source/livingroom_tour.mp4')
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
result = cv2.VideoWriter("result/livingroom_tour_copy.avi", fourcc, 50.0, (700,480))

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
