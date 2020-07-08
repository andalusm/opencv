import cv2
import numpy as np

img = cv2.imread("resources/lena.png")
#put images together horizontal
hor = np.hstack((img,img))




cv2.imshow("Horizontal images" ,hor)

cv2.waitKey(0)