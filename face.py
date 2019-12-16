import cv2 # opencv module

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # opencv frontalface properties
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') # opencv eye properties 

cap = cv2.VideoCapture(0) # live stream with camera

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 2, 5)
    
    for (x,y,w,h) in faces: 
        cv2.rectangle(img, (x,y) , (x+w, y+h),(255,0,0),2)
        roi_gray = gray[y:y+h , x:x+w] # important for eye
        roi_color = img[y:y+h , x:x+w] # important for eye
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew, ey+eh),(0,255,0),2)
        
            
    cv2.imshow('img', img) # !important!
    k = cv2.waitKey(30) & 0xff # 0xff:255
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()