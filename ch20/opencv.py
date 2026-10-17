import cv2
import matplotlib.pyplot as plt

image = cv2.imread(f'ch20\yamu_jay-friends-selfie-9129598_640.jpg')
face_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_path)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,
                                      scaleFactor=1.1,
                                      minNeighbors=5,
                                      minSize=(30,30))
for (x,y,w,h) in faces :
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('face',image)
cv2.waitKey(0)
cv2.destroyAllWindows