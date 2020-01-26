import cv2 as cv
import paho.mqtt.client as mqtt
import time

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv.VideoCapture(1)
haar_model = './haarcascade_frontalface_default.xml'
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
    img = cv.imshow('frame', gray)
    print(faces)
    for (x,y,w,h) in faces:
	# your logic goes here; for instance
	# cut out face from the frame.. 
        face = gray[y:y+h, x:x+w]
        rc,png = cv.imencode('.png', face)
        msg = png.tobytes()
	
	# Publish the message to the mqtt topic face_app
        local_mqttclient.publish(LOCAL_MQTT_TOPIC, msg, qos=1)

	# Show the cropped face on the window frame
        cv.imshow('crop', face)
	# Wait for 10 seconds or until a key is pressed
        key = cv.waitKey(10000)

    # look fpr the escape key on the frame window to exit
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()

# End the mqtt loop
local_mqttclient.loop_stop()
