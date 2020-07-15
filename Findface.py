import cv2
#check this for reference https://www.murtazahassan.com/learn-opencv-in-3-hours-chapter-9/

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    # we want to add rectangle to the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(img, "QUEEN", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2)


    cv2.imshow("Capture", img)
    #add delay to img for each frame and if clicked q it exits
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
