import paho.mqtt.client as mqtt
from datetime import datetime
import time

LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_PORT=1883
MQTT_TOPIC="face_app"

REMOTE_MQTT_HOST="169.44.155.180"
REMOTE_MQTT_PORT=1883

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(MQTT_TOPIC, 1)
	
def on_subscribe_local(client, userdata, flags, rc):
    print('subscribed to', MQTT_TOPIC)

def on_connect_remote(client, userdata, flags, rc):
    print("connected to remote broker with rc: " + str(rc))
	
def on_message(client,userdata, msg):
  try:
    print("message received!!!")
#    print(msg.payload)	
#    file_name = '/data_output_mqtt_' + str(current_time) + '.png'
#    msg_file = open(file_name, 'wb')
#    msg_file = open('/data_output_mqtt' + str(face_counter) + '.png', 'wb')
#    msg_file.write(msg.payload)
#    msg_file.close()
#    face_counter = face_counter + 1

    # if we wanted to re-publish this message, something like this should work
    msg = msg.payload
    remote_mqttclient.publish(MQTT_TOPIC, payload=msg, qos=1, retain=False)
    print('published message to remote')
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.on_message = on_message
local_mqttclient.on_subscribe = on_subscribe_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

remote_mqttclient = mqtt.Client()
remote_mqttclient.on_connect = on_connect_remote
remote_mqttclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)

# go into a loop
remote_mqttclient.loop_start()
local_mqttclient.loop_forever()
remote_mqttclient.loop_stop()
