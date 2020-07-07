import cv2

#We need to read an image
img = cv2.imread("resources/lena.png")

#convert the image into
#Grayscale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Blur it takes image the scale (has to be odd numbers) and sigmaX
imgBlur = cv2.GaussianBlur(img,(7,7),0)


cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur image",imgBlur)
cv2.waitKey(0)
