import cv2

#Check this https://www.murtazahassan.com/learn-opencv-in-3-hours-project-3/

#We want to detect car plate numbers via webcam

#We start with copying the webcam code from chapter 1
#Prameters-------
frameWidth = 640
frameHeight = 480
#changed this to plate number
nPlateCascade = cv2.CascadeClassifier("resources/haarcascade_russian_plate_number.xml")
minArea = 500
color = (255,0,255)
#####------------
count = 0
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
#we take code for casscade from chapter 9 and add it
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        #we want the area larger than a certain area
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            #we want to label it (we want the y a bit higher
            cv2.putText(img, "Number Plate", (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            #we want to save the number plate so we first crop it
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow("ROI", imgRoi)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        #we want to save the number plate if we exited
        #write image to
        cv2.imwrite("resources/scanned/NoPlate_" + str(count) + ".jpg", imgRoi)
        #we wat to create rectangle with text that tells us the image was saved
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                    2, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1