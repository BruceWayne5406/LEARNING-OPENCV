#reading images in opencv

import cv2 

img=cv2.imread("tejveersingh/spaceship.png")#this is used for reading a given image and returns it as a matrix of pixels
                                            #path to the image is given as the parameter in this function

cv2.imshow("image",img)# this function displays the image as a new window

cv2.waitKey(0)#this function with 0 as a parameter is used to display the image for infinite time

#reading videos using opencv



