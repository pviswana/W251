import numpy as np
import cv2 as cv

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv.VideoCapture(1)
haar_model = '/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv.CascadeClassifier(haar_model)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # We don't use the color information, so might as well save space
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # face detection and other logic goes here
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces)
    print(frame)
    for (x,y,w,h) in faces:
	# your logic goes here; for instance
	# cut out face from the frame.. 
        face = cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	rc,png = cv.imencode('.png', face)
	msg = png.tobytes()
        
        msg_file = open('./data_output.png', 'wb')
        msg_file.write(msg)
        msg_file.close()

    cv.imshow('img', frame)
    cv.waitKey(10000)
    cv.destroyAllWindows()
    break
