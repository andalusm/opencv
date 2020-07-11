import cv2
import numpy as np
#check this for reference https://www.murtazahassan.com/learn-opencv-in-3-hours-chapter-7-2/


#this function detects the shapes and adds a colored square around them
def getContours(img):
    #this function finds contours
    #it takes image, retreval method (this ones detects the extreme edges)
    # ,approximation (how many points you want to get we got all)
    contours , hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #we want to loop through them
    for cnt in contours:
        #for each countor we need to find the area
        area = cv2.contourArea(cnt)
        #printing it
        print(area)

        # we need to get rid of noise in the image so the area should have a threshold
        if area > 500:
            # we need to draw the contours, we need image to draw contour on, contours,
            # contours index (we put -1 to draw everything), color, thickness
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            #we need to approximate the edges so we are using this takes the contours and if the shape is closed or not
            peri = cv2.arcLength(cnt, True)
            print(peri)
            #approximate how many cornors we have, it give us the points themselves
            # we give contours and resolution(we can play around with it and if it is close
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
            #we find how many points
            print(len(approx))
            objCor = len(approx)
            #if we have to draw a pounding box around th shape what is the x,y,width,height
            x, y, w, h = cv2.boundingRect(approx)
            #we want to draw the recktangle around the shape so
            #we give the image, two points, color,thickness
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)



#adding stack function
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


path = 'Resources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()

#We need to convert to grayscale to see the difference to the background
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#we now need to add blur
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
#we need to find the edges in our images
#we gues the threshold
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
#we want an empty image
imgBlank = np.zeros_like(img)

imgStack = stackImages(0.6,([img,imgGray,imgBlur]
                            ,[imgCanny,imgContour,imgBlank]))

cv2.imshow("Image stack",imgStack)

cv2.waitKey(0)