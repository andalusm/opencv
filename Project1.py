import cv2


#we take the code from  the webcam in chapter 1
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)

while True:
    success, img = cap.read()
    cv2.imshow("Capture", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
