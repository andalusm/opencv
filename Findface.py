import cv2
import random

#A small project I wrote to find images and put a nickname filter on it
#I will expand on it later

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)

tagger = ["CUTE","QUEEN","BREATHTAKING","HEARTBREAKER","PRINCESS"]
rand = random.randint(0,len(tagger))
# we can also add a color for each nickname

while True:
    #we want each face to get a tag
    start = rand
    success, img = cap.read()
    #Flip the image horozintally so it can be a mirror
    img = cv2.flip(img, 1)
    faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detect faces
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    # we want to add rectangle to the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(img, tagger[start], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 255), 2)
        #to catch the errors if the array overflow
        start = (start + 1)%len(tagger)


    cv2.imshow("Capture", img)
    #add delay to img for each frame and if clicked q it exits
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
