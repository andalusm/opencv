import cv2

#==============================
##========Read Image===========
#==============================


#We need to read an image
img = cv2.imread("resources/lena.png")

#we need to show the image (takes name of window and img)
cv2.imshow("Output2",img)

#it goes away quickly we need to add deley
# 0=inf and everything else is how many mili second
cv2.waitKey(0)