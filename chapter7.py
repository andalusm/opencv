import cv2
import numpy as np
#check this for reference https://www.murtazahassan.com/learn-opencv-in-3-hours-chapter-7/

def empty(a):
    pass

#to make it look better we are adding the previous stacking function
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
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
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

path = "resources/lambo.png"
#adding track bars
cv2.namedWindow("TrackBars")
#resize the trackbars to fit
#should have the same name as before
cv2.resizeWindow("TrackBars",640,240)
#creating a track bar
#name of trackbar, name of window it is on, initial value,
# max value (hue are usually 255 but HSV has 179), function that runs everytime the value is changed
#tldr: (trckbar name, window name, init,max,function onchange)
#changing the init values to these (0 55 51 255 162 255)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",55,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",51,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",162,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)




#so we can get trcker value if changed we can do this
while True:
    img = cv2.imread(path)

    #convert to HSV
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #get value in trackbar

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    #print the values
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    #we make a mask for the image where it is between two numbers
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    #i making it we need to keep the colors we want as white and the others are black
    mask = cv2.inRange(imgHSV,lower,upper)
    #I got that the numbers are (0 55 51 255 162 255)

    #using the mask to create an image bitwise checks if white and takes it other wise it's black
    #add imges and the mask
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    #The stacked images
    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    cv2.imshow("Stacked Images", imgStack)


    # cv2.imshow("Original",img)
    # cv2.imshow("HSV",imgHSV)
    # cv2.imshow("Mask",mask)
    # cv2.imshow("Orange",imgResult)
    #change the wait so it can continue going through the loop
    cv2.waitKey(1)
