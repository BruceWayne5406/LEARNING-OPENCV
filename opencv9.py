#making technique essentially refers to focusing on different parts of an image while ignoring the rest of the part
import cv2
import numpy as np

blank=np.zeros((500,500,3),dtype="uint8")
cv2.imshow("blank image",blank)

img=cv2.imread("./spaceship.png")
resized=cv2.resize(img,(500,500))

cv2.imshow("resized image",resized)

mask=cv2.circle(blank,(250,250),40,(255,255,255),thickness=-1)
cv2.imshow("mask",mask)

masked=cv2.bitwise_and(resized,mask)
cv2.imshow("masked image",masked)

cv2.waitKey(0)