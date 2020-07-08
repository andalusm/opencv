import cv2
import numpy as np
#check this for reference https://www.murtazahassan.com/learn-opencv-in-3-hours-chapter-7/

path = "resources/lambo.png"

img = cv2.imread(path)

#convert to HSV
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)



cv2.imshow("Original",img)
cv2.imshow("HSV",imgHSV)
cv2.waitKey(0)
