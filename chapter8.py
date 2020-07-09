import cv2
import numpy as np
#check this for reference https://www.murtazahassan.com/learn-opencv-in-3-hours-chapter-7-2/

path = 'Resources/shapes.png'
img = cv2.imread(path)

#We need to convert to grayscale to see the difference to the background
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#we now need to add blur
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)


cv2.imshow("Original",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)

cv2.waitKey(0)