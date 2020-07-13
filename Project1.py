import cv2
import numpy as np


#we take the code from  the webcam in chapter 1
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)
#List of colors we want to detect we found them using Color picker
myColors = [[0,111,0,9,255,255],
            [29,24,0,104,88,117]]

#this function should find colors and detect them and show them via mask
def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #added to detect all colors
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        #send mask to get contours
        getContours(mask)
        # cv2.imshow(str(color),mask)

#we need to approximate the bounding box around it
def getContours(img):
    contours , hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)



while True:
    success, img = cap.read()
    imgResult = img.copy()
    findColor(img, myColors)
    #we want to display it with contour
    cv2.imshow("Capture", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
