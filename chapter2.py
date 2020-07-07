import cv2
import numpy as np

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
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)


cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dilated image",imgDilation)


cv2.waitKey(0)
