#essential functions in opencv

import cv2

img=cv2.imread("./spaceship.png")
cv2.imshow("image",img)

#converting coloured image to a grayscale image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image",gray)

#blurring the image
blur=cv2.GaussianBlur(img,(7,7),cv2.BORDER_DEFAULT)#here (7,7) is the kernel size
cv2.imshow("blurred_image",blur)

#edge cascading
canny=cv2.Canny(blur,125,175)#here 125,175 are the threshiold values
cv2.imshow("canny image",canny)

#dilating an image
dilated=cv2.dilate(canny,(7,7),iterations=3)
cv2.imshow("dilated image",dilated)

#eroding an image
eroded=cv2.erode(canny,(7,7),iterations=3)
cv2.imshow("eroded image",eroded)

#resizing an image
resized=cv2.resize(img,(400,400))
cv2.imshow("resized image",resized)

#cropping
cropped=img[50:200,200:400]#images can be treated as arrays as they are nothing but an array of pixels
cv2.imshow("cropped image",cropped)

cv2.waitKey(0)
