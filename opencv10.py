import cv2
import numpy as np
import matplotlib.pyplot as plt

blank=np.zeros((500,500,3),dtype="uint8")
cv2.imshow("blank image",blank)

img=cv2.imread("./ufo-2.png")
cv2.imshow("coloured image",img)

resized=cv2.resize(img,(500,500))

cv2.imshow("image",resized)

gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image",gray)
mask=cv2.circle(blank,(250,250),50,(255,255,255),thickness=-1)
masked=cv2.bitwise_and(resized,mask)

cv2.imshow("masking",masked)
colors=("b","g","r")

for i , col in enumerate(colors):
     hist=cv2.calcHist([resized],[i],None,[256],[0,256])#this function receives a series of arguments including list of images(gray here..),
#index of the scale of the image(0 here..), masks if any , histsize or bins, and the range of all possible pixel values. 
     plt.plot(hist)
    
     plt.xlim([0,256])

plt.xlabel("bins")
plt.ylabel("no.of pixels")
plt.title("BGR scale histogram")


plt.show()


cv2.waitKey(0)
