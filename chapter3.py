import cv2
# can also check https://www.murtazahassan.com/chapter-3/
img = cv2.imread("resources/lambo.png")

#before resizing we need to know the shape
#I got (462, 623, 3)
print(img.shape)

#resizing put width then height (we can increase or decrease the size)
imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)

#Cropping image height first then with
imgCrop = img[0:200,200:500]


cv2.imshow("Image",img)
cv2.imshow("Image Resized",imgResize)
cv2.imshow("Image Cropped",imgCrop)


cv2.waitKey(0)