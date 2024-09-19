#face detection using haarcascades in opencv(do not confuse face dtection with face recognition)
#face detection is performed using classifiers
#a classifier is an algorithm that determines whether an image is positive or negative
#i.e whether it has a face or not
#haarcascades is a predefined classifier from opencv among many others
#such as local binary ptterns which is a more advanced classifier than haarcascades
#haarcascades is very sensitive to noise,so while building more advanced openCV projects ,we tend to use other classifiers



import cv2

img=cv2.imread("./faces.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale",gray)

haar_cascade=cv2.CascadeClassifier("my_pic.xml")

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)#faces_rect is simply a list of rectangles formed over the faces

print(f"number of faces found = {len(faces_rect)}")

for (x,y,w,h) in faces_rect:#for detecting multiple faces and drawing multiple rectangles,we implement a for loop.
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv2.imshow("detected faces",img)


cv2.waitKey(0)


