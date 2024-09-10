#here we are going to deal with edge detection
#mainly we are going to talk about 2 methods i.e laplacian method
#and the sobel method

#although we have used the canny edge detector previously...
#but that is just an advanced version of sobel in the sense that it uses sobel
#like thresholding,edge detection is done on grayscale images



import cv2
import numpy as np

img=cv2.imread("./spaceship.png")
resized=cv2.resize(img,(500,500))
gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)

cv2.imshow("image",gray)

# starting with the laplacian method
lap=cv2.Laplacian(gray,cv2.CV_64F)#here cv2.cv_64f is the data depth
lap=np.uint8(np.absolute(lap))
cv2.imshow("laplacian",lap)

#sobel method
sobelx=cv2.Sobel(gray,cv2.CV_64F,1,0)#refers to the gradients or edges that are computed along the x axis(here 1,0 refers to x,y coordinate respectively)
sobely=cv2.Sobel(gray,cv2.CV_64F,0,1)#refers to the gradients or edges computed along the y axis
combined=cv2.bitwise_or(sobelx,sobely)#combining the edges computed in both sobel x&y 
canny=cv2.Canny(gray,150,175)#Canny is actually a more advanced algorithm for edge detection that actually uses sobel in one of its stages


cv2.imshow("sobel_x",sobelx)
cv2.imshow("sobel_y",sobely)
cv2.imshow("combing sobel x&y",combined)
cv2.imshow("canny edge detector",canny)






cv2.waitKey(0)