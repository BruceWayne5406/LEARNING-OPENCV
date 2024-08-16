#drawing shapes and put text using opencv

import cv2
import numpy as np

#now there are 2 ways to start drawing using opencv
#one in which we start drawing over existing images
#second in which we create an image of a blank page and we draw on that

blank=np.zeros((500,500,3),dtype="uint8")#this creates a blank image of 500 by 500 and the datatype is uint8 i.e data type of an image
                                        #500,500,3 are respectively height,width and the number of colour channels
cv2.imshow("blank_image",blank)

#1 to paint the image a certain colour.
blank[:]=0,0,255# here we are colouring all the pixels of the array as red
cv2.imshow("coloured_img",blank)

#we can also colour a certain portion of the blank space by giving a range of pixels
blank[200:300,300:400]=0,255,0
cv2.imshow("green_img",blank)

#drawing a rectangle
cv2.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)
cv2.imshow("rectangle",blank)#if we wanted a ractangle filled with green colour
                            #we would put thickness=-1

#the parameters are respectively the image over which the triangle has to be
#,point1,point2,colour used,thickness

#drawing a circle
cv2.circle(blank,(200,200),40,(255,255,255),thickness=-1)
cv2.imshow("circle_img",blank)

#drawing a line
cv2.line(blank,(100,200),(400,200),(0,0,255),thickness=2)
cv2.imshow("line_img",blank)

#write text
cv2.putText(blank,"hello world",(100,100),cv2.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv2.imshow("text_img",blank)





cv2.waitKey(0)