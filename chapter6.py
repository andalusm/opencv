import cv2
import numpy as np

img = cv2.imread("resources/lena.png")
#put images together horizontal
imgHor = np.hstack((img, img))
#put images together vertical
imgVer = np.vstack((img,img))


cv2.imshow("Horizontal images", imgHor)
cv2.imshow("Vertical images",imgVer)
cv2.waitKey(0)