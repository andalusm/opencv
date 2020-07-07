import cv2
import numpy as np
#check this out https://www.murtazahassan.com/learn-opencv-in-3-hours-chapter-4/

# we add the size and the number of channels for the colors
img = np.zeros((512,512,3), np.uint8)

#coloring the image
# # we make it blue (reminder [:] is all) (255,0,0 is blue)
img[:] = 255,0,0
#print(img)

#adding lines to image
#we say from where the start is to where the end is then the color (red) and the thickness
# (start point),(end point(we can put width and height to get the end),(color BGR), (thickness (default 1)
cv2.line(img,(200,0),(300,300),(0,0,255),3)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,255,255),3)

#adding rectangle (same thing as above)
cv2.rectangle(img,(0,0),(250,350),(0,0,0),2)
#if we want to fill it we replace the thickness with cv2.FILLED
cv2.rectangle(img,(300,300),(400,500),(0,255,0),cv2.FILLED)



cv2.imshow("Image",img)
cv2.waitKey(0)
