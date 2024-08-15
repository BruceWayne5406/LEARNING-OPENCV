#reading images in opencv

import cv2 

img=cv2.imread("tejveersingh/spaceship.png")#this is used for reading a given image and returns it as a matrix of pixels
                                            #path to the image is given as the parameter in this function

cv2.imshow("spaceship",img)# this function displays the image as a new window


#reading videos using opencv

capture=cv2.VideoCapture("tejveersingh/video.mp4")#this function can either take a path of the video as a parameter or integers such as 0,1,2
#the integer 0 is used to refer to the webcam you might have in your laptops. integers like 1,2,.. are used to refer to the externally..
#connected webcams that you might have

#in the case of reading videos , we use a while loop and read videos frame by frame

while True:
    isTrue,frame=capture.read()#this basically reads the video frame by frame,returing a boolean value and the frame
    cv2.imshow("video",frame)#this displays the video frame by frame

    if cv2.waitKey(20) and 0xFF==ord("d"):# this function is helping us to get out of this loop,if letter d is pressed
         #break                                   # and waitkey==20


capture.release()#releasing the capture device 
cv2.destroyAllWindows()#destroying all the windows since we dont need them anymore






cv2.waitKey(0)#this function with 0 as a parameter is used to display the image for infinite time


