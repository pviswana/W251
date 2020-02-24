import cv2 as cv
import paho.mqtt.client as mqtt
import io

from PIL import Image
import sys
import os
import urllib
import tensorflow.contrib.tensorrt as trt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import tensorflow as tf
import numpy as np
import time
from tf_trt_models.detection import download_detection_model, build_detection_graph

FROZEN_GRAPH_NAME = 'data/frozen_inference_graph_face.pb'
IMAGE_PATH = 'data/warriors.jpg'

output_dir=''
frozen_graph = tf.GraphDef()
with open(os.path.join(output_dir, FROZEN_GRAPH_NAME), 'rb') as f:
  frozen_graph.ParseFromString(f.read())

INPUT_NAME='image_tensor'
BOXES_NAME='detection_boxes'
CLASSES_NAME='detection_classes'
SCORES_NAME='detection_scores'
MASKS_NAME='detection_masks'
NUM_DETECTIONS_NAME='num_detections'

input_names = [INPUT_NAME]
output_names = [BOXES_NAME, CLASSES_NAME, SCORES_NAME, NUM_DETECTIONS_NAME]

trt_graph = trt.create_inference_graph(
    input_graph_def=frozen_graph,
    outputs=output_names,
    max_batch_size=1,
    max_workspace_size_bytes=1 << 25,
    precision_mode='FP16',
    minimum_segment_size=50
)

tf_config = tf.ConfigProto()
tf_config.gpu_options.allow_growth = True

tf_sess = tf.Session(config=tf_config)

# use this if you want to try on the optimized TensorRT graph
# Note that this will take a while
# tf.import_graph_def(trt_graph, name='')

# use this if you want to try directly on the frozen TF graph
# this is much faster
tf.import_graph_def(frozen_graph, name='')

tf_input = tf_sess.graph.get_tensor_by_name(input_names[0] + ':0')
tf_scores = tf_sess.graph.get_tensor_by_name('detection_scores:0')
tf_boxes = tf_sess.graph.get_tensor_by_name('detection_boxes:0')
tf_classes = tf_sess.graph.get_tensor_by_name('detection_classes:0')
tf_num_detections = tf_sess.graph.get_tensor_by_name('num_detections:0')

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv.VideoCapture(1)
#haar_model = './haarcascade_frontalface_default.xml'
#face_cascade = cv.CascadeClassifier(haar_model)

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

count = 0
while(True):
    start_time = time.time()

    # Capture frame-by-frame
    ret, frame = cap.read()
    print('frame type', type(frame))

    img = cv.imshow('frame', frame)
    rc1,image = cv.imencode('.png', frame)
    full_face_bytes = image.tobytes()
    f = open('output_' + str(count), 'wb')
    f.write(full_face_bytes)
    f.close()

    image = Image.open('output_' + str(count))

    image_resized = np.array(image.resize((300, 300)))
    image_array = np.array(image)

    scores, boxes, classes, num_detections = tf_sess.run([tf_scores, tf_boxes, tf_classes, tf_num_detections], feed_dict={
tf_input: image_resized[None, ...]
})

    boxes = boxes[0] # index by 0 to remove batch dimension
    scores = scores[0]
    classes = classes[0]
    num_detections = num_detections[0]

    print('face count', num_detections)
    DETECTION_THRESHOLD = 0.5

    # plot boxes exceeding score threshold
    for i in range(int(num_detections)):
        if scores[i] < DETECTION_THRESHOLD:
            continue

        # scale box to image coordinates
        box = boxes[i] * np.array([image_array.shape[0], image_array.shape[1], image_array.shape[0], image_array.shape[1]])

        print('processing detection #: ', i)
        #box = boxes[i]
        print('box values')
        print('box0', box[0])
        print('box1', box[1])
        print('box2', box[2])
        print('box3', box[3])

        img_face = image.crop((box[1], box[0], box[3], box[2]))
        img_face.save('output_face_' + str(count) + '.png')

        imgByteArr = io.BytesIO()
        img_face.save(imgByteArr, format='PNG')
        msg = imgByteArr.getvalue()

        end_time = time.time()
        print('Counter ' + str(count) + ' time:', (end_time - start_time))

        f = open('output_face_bytes_' + str(count) + '.png', 'wb')
        f.write(msg)
        f.close()

	# Publish the message to the mqtt topic face_app
        local_mqttclient.publish(LOCAL_MQTT_TOPIC, msg, qos=1)

    # look fpr the escape key on the frame window to exit
    key = cv.waitKey(1000)
    if key == 27:
        break
    count = count + 1

cap.release()
cv.destroyAllWindows()

tf_sess.close()

# End the mqtt loop
local_mqttclient.loop_stop()
