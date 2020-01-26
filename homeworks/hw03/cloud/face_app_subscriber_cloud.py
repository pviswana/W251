import paho.mqtt.client as mqtt
from datetime import datetime
import time

LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="face_app"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client,userdata, msg):
  try:
    current_time = time.strftime("%Y%m%d%H%M%S")
    print('current time', current_time)
    print('size of payload', msg.payload)
    print("message received!!!" + str(current_time))
    file_name = '/mnt/hw3bucket/face_image_' + str(current_time) + '.png'
    msg_file = open(file_name, 'wb')
    msg_file.write(msg.payload)
    msg_file.close()

  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
