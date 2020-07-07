import cv2

#We need to read an image
img = cv2.imread("resources/lena.png")

#convert the image into
#Grayscale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.imshow("Gray image",imgGray)
cv2.waitKey(0)
