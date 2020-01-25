import paho.mqtt.client as mqtt
from datetime import datetime
import time

LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="test"

face_counter = int(0)
current_milli_time = lambda: int(round(time.time() * 1000))

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client,userdata, msg):
  try:
#    current_time = datetime.now().time()
    current_time = current_milli_time()
    print("message received!!!" + str(current_time))
#    print(msg.payload)	
    file_name = '/data_output_mqtt_' + str(current_time) + '.png'
    msg_file = open(file_name, 'wb')
#    msg_file = open('/data_output_mqtt' + str(face_counter) + '.png', 'wb')
    msg_file.write(msg.payload)
    msg_file.close()
    face_counter = face_counter + 1

    # if we wanted to re-publish this message, something like this should work
    # msg = msg.payload
    # remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message



# go into a loop
local_mqttclient.loop_forever()
