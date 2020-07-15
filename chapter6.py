import cv2
import numpy as np
#Check this for reference https://www.murtazahassan.com/learn-opencv-in-3-hours-chapter-6/

#Learning to stack images together vertically and horrozintally

#added this function to handle it
#it needs the scale and array
#the array has to be nxm and can't be missing elements
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list) #checks if the first column is a list
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]: #checks if all of them have the same lheight and width
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)#does nothing
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)#matches the sizes
                if len(imgArray[x][y].shape) == 2:#if the image is gray turns it to BGR
                    imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8) #Builds the normal img
        hor = [imageBlank]*rows #builds all images combined matrix
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])#combines all images horizontal
        ver = np.vstack(hor)#combines them vertical
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

img = cv2.imread("resources/lena.png")
# #put images together horizontal
# imgHor = np.hstack((img, img))
# #put images together vertical
# imgVer = np.vstack((img,img))
# #the problems with this is the images can't be resized so if you want more images
# #it might go out of frame and also they need to be the same number of channels(can't one be gray and one RGB)

imgStack = stackImages(0.5,([img,img,img],[img,img,img]))
cv2.imshow("Stacked images", imgStack)
# cv2.imshow("Horizontal images", imgHor)
# cv2.imshow("Vertical images",imgVer)
cv2.waitKey(0)