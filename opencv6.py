#contours in opencv can be thought of as edges in the image
#however mathematically it si not coreect to think of them as edges
#but for the programming part it is fine to take that approach

import cv2
import numpy as np

img=cv2.imread("./spaceship.png")
cv2.imshow("image",img)

resized=cv2.resize(img,(600,600))
cv2.imshow("bigger image",resized)

gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image",gray)

blank=np.zeros((600,600,3),dtype="uint8")
cv2.imshow("blank image",blank)

blur=cv2.GaussianBlur(gray,(7,7),cv2.BORDER_DEFAULT)
cv2.imshow("blurred image",blur)

canny=cv2.Canny(blur,125,175)#edge cascading
cv2.imshow("edges cascaded",canny)

#ret,thresh=cv2.threshold(gray,125,175,cv2.THRESH_BINARY)
#cv2.imshow("thresh",thresh)

contours,hierarchies=cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
#contours is a list here

print(f"{len(contours)} found!")

cv2.drawContours(blank,contours,-1,(0,0,255),1)
#-1 here means that we want to draw all the contours in the image
#1 is the thickness
#a list is one of the arguments of the above funtion that is why we put contours

cv2.imshow("contours drawn",blank)

cv2.waitKey(0)
