import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt
import time

face_counter = 0

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv.VideoCapture(1)
haar_model = './haarcascade_frontalface_default.xml'
#haar_model = '/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv.CascadeClassifier(haar_model)

LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="face_app"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

# go into a loop
local_mqttclient.loop_start()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # We don't use the color information, so might as well save space
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # face detection and other logic goes here
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces)
    for (x,y,w,h) in faces:
	# your logic goes here; for instance
	# cut out face from the frame.. 
        face = gray[y:y+h, x:x+w]
	rc,png = cv.imencode('.png', face)
	msg = png.tobytes()
        
        msg_file = open('./data_output' + str(face_counter) + '.png', 'wb')
        msg_file.write(msg)
        msg_file.close()

        local_mqttclient.publish(LOCAL_MQTT_TOPIC, msg, qos=1)

        cv.imshow('img', face)
        cv.waitKey(10000)

    cv.destroyAllWindows()
    if face_counter == 5:
    	break
    face_counter = face_counter + 1

    time.sleep(1) 


local_mqttclient.loop_stop()
