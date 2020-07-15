import cv2
import numpy as np

#https://www.murtazahassan.com/learn-opencv-in-3-hours-project-2/
#We will work on document scanner in this project



#this function is to preprocess the image and find the edges using the same as chapter 3 with canny
#we add dilate and erode since the edges are quite thin and if there are shadows or something it won't detect it
def preProcessing(img):
    #convert to grayscale then blur then canny then dilation and erode
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    kernel = np.ones((5, 5))
    imgDilated = cv2.dilate(imgCanny, kernel, iterations=2)
    imgEroded = cv2.erode(imgDilated, kernel, iterations=1)
    return imgEroded

#we used what we used in chapter 8 to find countours in img that we preprocessed
#we copy get contours from chapter 8
def getContours(img):
    #initiate the values
    biggest = np.array([])
    maxArea = 0
    contours , hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #add another zero since the page will be very big
        if area > 5000:
            # cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
            #since it is a page it has 4 edges so we only want that shape and only the biggest page will be choosen
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 3)
    return biggest

#this function is made to correctly order the points
#the first x+y gives min, the last point x+y is max
#the second x-y is positive and the third x-y is negative
def reorder(myPoints):
    #shape of biggest is (4,1,2) we first reshape it since the 1 is useless and will make it more difcult
    myPoints = myPoints.reshape((4,2))
    #what we return is matrix that has shape (4,1,2)
    myPointsNew = np.zeros((4,1,2),np.int32)
    #to find the max and min we find via sum
    add = myPoints.sum(1)
    # print("add", add)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    #to find the smallest we find via differance between the numbers
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    # print("NewPoints",myPointsNew)
    return myPointsNew



#we want to use warp perspective like what we did in chapter 5
#this code is uncorrect since we don't know the order of biggest
def getWarp(img,biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    #it has a few lines added we want to crop them out
    imgCropped = imgOutput[20:imgOutput.shape[0] - 20, 20:imgOutput.shape[1] - 20]
    #after removing 20px from each side we resize the image again to fit
    imgCropped = cv2.resize(imgCropped, (widthImg, heightImg))
    return imgCropped



#img size
widthImg = 640
heightImg = 480
#we want the code from the webcam from chapter 1
cap = cv2.VideoCapture(0)
# cap.set(3, widthImg)
# cap.set(4, heightImg)
cap.set(10,150)
while True:
    success, img = cap.read()
    # we want to resize it
    img = cv2.resize(img, (widthImg, heightImg))
    imgContour = img.copy()
    imgThres = preProcessing(img)
    biggest = getContours(imgThres)
    print(biggest)
    if biggest != []:
        imgWarped = getWarp(img,biggest)
        cv2.imshow("Result", imgWarped)
    else:
        cv2.imshow("Result", imgContour)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break