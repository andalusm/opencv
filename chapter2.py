import cv2
import numpy as np
#can also check this https://www.murtazahassan.com/learn-opencv-in-3-hours-chapter-2/

#We will learn how to add different effects to images in OpenCV

#We need to read an image
img = cv2.imread("resources/lena.png")

#add matrix there are 5x5 cells and the numbers are from 0 to 255
kernel = np.ones((5,5),np.uint8)

#convert the image into
#Grayscale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Blur it takes image the scale (has to be odd numbers) and sigmaX
imgBlur = cv2.GaussianBlur(img,(7,7),0)
#Canny finds edges in image add threshold
imgCanny = cv2.Canny(img,200,150)
#dilation better defies the borders of the canny image
# we need a matrix so install numpy for this step
# iterations is the thickness
imgDilated = cv2.dilate(imgCanny,kernel,iterations=1)
#eroded is the oppesite of Dilate it gives smaller lines
imgEroded = cv2.erode(imgDilated,kernel,iterations=1)


cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dilated image",imgDilated)
cv2.imshow("Eroded image",imgEroded)


cv2.waitKey(0)
