
# Set up and execution process

## IBM Cloud
### VSI
* A virtual server instance was created on the ibm cloud with 1CPU and 1GB ram.

### Object Store
* A new object store was created on the IBM cloud
* The HMAC information of the Object store was saved with the Key Id and the Secret Key to be used later for mounting the buckets created on the object store 

### Mosquitto Broker
* A docker image named alpine_mosquitto was created from alpine with mosquitto installed
   * Dockerfile.alpine-mosquitto
* A docker container was started with the name alpine_mosquitto
* The mosquitto process was then kicked off within this docker container to act as the broker for this machine
* We also started the container with the option -p 1883:1883 so that we can have access to the broker from the public ip address

### Face App subscriber and file saver program
* A docker image named face-app-ubuntu-mqtt-py was created from the docker file Dockerfile.ubuntu-mqtt-py
  * This is an ubuntu with paho mqtt installed
* A docker container was started using this image with the script docker_run_face_app.sh
  * The docker container was started using the same network config as the mosquitto broker
* s3fs was installed in the container and the ibm cloud object storage bucket was mounted to /mnt/hw3bucket
  * All the files from the bucket was now visible in this directory
* We then started the python program face_app_subscriber_cloud.py within this container
  * Connects to the mqtt broker
  * Subscribes to the topic face_app
  * On receiving the file bytes of the images, it saves it to the mounted directory /mnt/hw3bucket
  * The file names were appended with timestamp to make them unique

# Links to image files
* https://w251-cloud-object-storage-j3-cos-standard-0js.s3.us-south.cloud-object-storage.appdomain.cloud/face_image_20200125213800.png
* https://w251-cloud-object-storage-j3-cos-standard-0js.s3.us-south.cloud-object-storage.appdomain.cloud/face_image_20200125213757.png



## Jetson TX2
### Hardware setup
* Connected the logitech camera to the usb hub connected to the Jetson TX2

### Network Bridge for local mqtt communication
* Created a local network bridge using the following command
  * docker network create --driver bridge w251hw03
* docker_network_start.sh

### Mosquitto Broker
* Created a docker image to run the mosquitto broker with alpine and mosquitto using the following docker file
  * Dockerfile.alpine-mosquitto
* Started a docker container using the network w251hw03 and with other options using the script `mqtt_broker_tx2_start.sh`

### Subscriber and remote publisher
* Created a docker image from alpine with mosquitto client, paho-mqtt using `Dockerfile.alpine-mqtt-py`
* Started a docker container using the same network w251hw03 so that we can connect to the local broker 
  * subscriber_start.sh
* Started the python program called face_app_subscriber_tx2.py
  * Subscribes to the local broker for topic `face_app`
  * Connects to the remote broker running on the cloud
  * On message receipt it publishes the message to the remote connection 
  * The QoS = 1 indicates we want to sent the message atleast once

### Face Detection Program
* Created a docker image from ubuntu with mosquitto client, paho-mqtt, opencv using `Dockerfile.opencv-mqtt`
* Started a docker container using the same network w251hw03 so that we can connect to the local broker 
  * face_app_start.sh
* Started the python program called facedetection.py
  * Connects to the local broker
  * Captures image from the camera using opencv
  * Crops the face from the image
  * Converts the image to bytes
  * Sends the converted bytes to the message infrastructure using the topic `face_app`
  * The QoS = 1 indicates we want to sent the message atleast once
  * Continues to wait for the next face on the camera and sends the bytes if found
  * The program quits when the escape key is pressed
