import cv2
import numpy as np
#check the code at https://www.murtazahassan.com/learn-opencv-in-3-hours-chapter-5/

img = cv2.imread("resources/cards.jpg")

#the size of the new image
width,height = 250,350
#first after figuring out (by paint) the points put them in
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
#second we figure out where to put them
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
#warping the image 2 steps
#the transformation matrix
#the starting points the ending points
matrix = cv2.getPerspectiveTransform(pts1,pts2)
#warping the image
#we need matrix,width and height of the final image
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("The whole image",img)
cv2.imshow("Card",imgOutput)
cv2.waitKey(0)