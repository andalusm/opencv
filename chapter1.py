import cv2

#==============================
##========Read Image===========
#==============================


#We need to read an image
img = cv2.imread("resources/lena.png")

#we need to show the image (takes name of window and img)
cv2.imshow("Output1",img)

#it goes away quickly we need to add deley
# 0=inf and everything else is how many mili second
cv2.waitKey(0)

#==============================
##========Read Video===========
#==============================

#we need to read a video
vid = cv2.VideoCapture("resources/test_video.mp4")

#to read the video we have to save each image of it alone and run one by one
while True:
    #return sucess if it read the image and save this image frame in a variable
    success, img = vid.read()
    # we need to show the image frame (takes name of window and img)
    cv2.imshow("Output2", img)
    #add delay to img for each frame and if clicked q it exits
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


