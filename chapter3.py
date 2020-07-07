import cv2

img = cv2.imread("resources/lambo.png")

#before resizing we need to know the shape
#I got (462, 623, 3)
print(img.shape)

#resizing put width then height (we can increase or decrease the size)
imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)

cv2.imshow("Image",img)
cv2.imshow("Image Resized",imgResize)


cv2.waitKey(0)