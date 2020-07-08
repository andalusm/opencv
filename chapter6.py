import cv2
import numpy as np

img = cv2.imread("resources/lena.png")
#put images together horizontal
imgHor = np.hstack((img, img))
#put images together vertical
imgVer = np.vstack((img,img))
#the problems with this is the images can't be resized so if you want more images
#it might go out of frame and also they need to be the same number of channels(can't one be gray and one RGB)


cv2.imshow("Horizontal images", imgHor)
cv2.imshow("Vertical images",imgVer)
cv2.waitKey(0)