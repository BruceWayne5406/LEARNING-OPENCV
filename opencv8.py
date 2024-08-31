#bitwise operations are basucally operations used in image processing
#they include bitwise_and,bitwise_or, bitwise_not and bitwise_xor

import cv2
import numpy as np

blank=np.zeros((500,500,3),dtype="uint8")

rectangle=cv2.rectangle(blank,(0,0),(250,250),(255,255,255),thickness=-1)
cv2.imshow("rectangle image",rectangle)

circle=cv2.circle(blank,(280,280),50,(255,255,255),thickness=-1)
cv2.imshow("circle image",circle)

#using bitwise operators here

bitwise_and=cv2.bitwise_and(rectangle,circle)#this operator returns the intersection of two images
cv2.imshow("and_image",bitwise_and)

bitwise_or=cv2.bitwise_or(rectangle,circle)#this returns the intersecting as well as the non intersecting region
cv2.imshow("or image",bitwise_or)

bitwise_xor=cv2.bitwise_xor(rectangle,circle)#this operator returns the non-intersecting regions
cv2.imshow("xor image",bitwise_xor)

bitwise_not=cv2.bitwise_not(circle)#this operator just inverts the image,hence black pixels become white and vice versa
cv2.imshow("not image",bitwise_not)

cv2.waitKey(0)