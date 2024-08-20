import cv2
import numpy as np

img=cv2.imread("./spaceship.png")
cv2.imshow("image",img)

resized=cv2.resize(img,(500,500))
cv2.imshow("resized image",resized)

#translating an image in the coordinate plane
def translate(img,x,y):
    trans_mat=np.float32([[1,0,x],[0,1,y]])#to translate an image we need to create a translation matrix
    dimensions=(500,500)#width , height respectively
    return cv2.warpAffine(img,trans_mat,dimensions)

translated=translate(resized,-100,100)
cv2.imshow("translated_image",translated)

#rotating an image in the coordinate plane
def rotation(img,angle,rot_point=None):
    rot_mat=cv2.getRotationMatrix2D(rot_point,angle,1.0)#similarly we need a rotation matrix for rotating an image
    dimensions=(500,500)#width and height respectively
    return cv2.warpAffine(img,rot_mat,dimensions)

rotated=rotation(resized,90)
cv2.imshow("rotated image",rotated)


cv2.waitKey(0)

