import cv2
import numpy as np

#get code at https://www.murtazahassan.com/learn-opencv-in-3-hours-project-1/

#We will work on a capture webcam that detects preset colors and draws them, the colors that is drawn are preset too

#we take the code from  the webcam in chapter 1
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)
#List of colors we want to detect we found them using Color picker
myColors = [[0,111,0,9,255,255],
            [29,24,0,104,88,117]]

#The colors in BGR
myColorValues = [[0,0,205],
                 [0,51,0]]

#in order to draw we need to save the points, we will save three inputs the x and y of the point and the colorId via the list
myPoints = []  ## [x , y , colorId ]

#this function should find colors and detect them and show them via mask
def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #added to detect all colors
    count=0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        #send mask to get contours and return middle point
        x,y=getContours(mask)

        #we add the new points only if it is not 0
        if x != 0 and y != 0:
            # draw circle on the image result
            cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
            newPoints.append([x, y, count])
        count+=1
        #cv2.imshow(str(color),mask)
    return newPoints

#we need to approximate the bounding box around it
def getContours(img):
    contours , hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #if it is not detected put 0
    x, y, w, h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    #we want to return the center of the shape
    return x+w//2,y
#in order to draw we need the point and the colors we used
def drawOnCanvas(myPoints,myColorValues):
    #we go through all the point and draw them
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)




while True:
    success, img = cap.read()
    imgResult = img.copy()
    #each time we get a new point we redraw all of them adding this point
    newPoints = findColor(img, myColors, myColorValues)
    #Check if we have points:
    if len(newPoints) != 0:
        #Add all new points to the old ones
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        #draw them
        drawOnCanvas(myPoints, myColorValues)
    #we want to display it with contour
    cv2.imshow("Capture", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
