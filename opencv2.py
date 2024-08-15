#resizing and rescaling images and video frames
#usually this is done to prevent computational strain


#resizing images in opencv
import cv2

img=cv2.imread("images/spaceship 11.56.20 AM.png")
resize=cv2.resize(img,(800,800))

cv2.imshow("originalpic",img)
cv2.imshow("resizedpic",resize)








cv2.waitKey(0)#to show the image till the close button is clicked
cv2.destroyAllWindows()#self explanatory

