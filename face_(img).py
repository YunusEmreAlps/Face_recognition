import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # frontal face library
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') # eye library

photo = cv2.imread('C:\\Users\\Dell\\Downloads\\Photo\\warren.jpg') # Somebody image
gray = cv2.cvtColor(photo, cv2.COLOR_RGB2GRAY) # grayscale

faces = face_cascade.detectMultiScale(gray) # face detector

for (x,y,w,h) in faces:   
    cv2.rectangle(photo,(x,y),((x+w),(y+h)),(255,0,0),2)

    
cv2.imshow('PhotoFace',photo) # PhotoFace(title),Show face -> (output) 
cv2.waitKey(0)
cv2.destroyAllWindows()
