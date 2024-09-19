import cv2
import numpy as np

people=["ben affleck","elton john","jerry seinfield","madonna","mindy kaling"]

haar_cascade=cv2.CascadeClassifier("my_pic.xml")
features=np.load("features.npy")
labels=np.load("labels.npy")

face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

img=cv2.imread("put multiple image paths here")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("uip",gray)

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

for (x,y,w,h) in faces_rect:
    faces_roi=gray[x:x+w,y:y+h]

    label,confidence=face_recognizer.predict(faces_roi)
    print(f"label={label} with a confidence of {confidence}")
    cv2.putText(img,str(people[label],(20,20),cv2.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2))
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv2.imshow("detected face",img)

cv2.waitKey(0)