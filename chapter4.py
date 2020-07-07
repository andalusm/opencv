import cv2
import numpy as np
#check this out https://www.murtazahassan.com/learn-opencv-in-3-hours-chapter-4/

# we add the size and the number of channels for the colors
img = np.zeros((512,512,3), np.uint8)

#coloring the image blue (reminder [:] is all) (255,0,0 is blue)
img[:] = 255,0,0
print(img)



cv2.imshow("Image",img)
cv2.waitKey(0)
