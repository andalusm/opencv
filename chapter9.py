import cv2

#check this for reference https://www.murtazahassan.com/learn-opencv-in-3-hours-chapter-9/

#find faces using cascade with a preset cascade


img = cv2.imread('Resources/lena.png')
#first we need face cascade which is the thing that detects faces
faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
#turn image to grayscale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#find faces using cascade , we need gray image ,scale factor, minimum neighbors
faces = faceCascade.detectMultiScale(imgGray,1.1,4)

#we want to add rectangle to the faces
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)