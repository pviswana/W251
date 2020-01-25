# Set up and execution process

## IBM Cloud
### VSI
* A virtual server instance was created on the ibm cloud with 1CPU and 1GB ram.

### Object Store
* A new object store was created on the IBM cloud
* The HMAC information of the Object store was saved with the Key Id and the Secret Key to be used later for mounting the buckets created on the object store 

### Mosquitto Broker
* A docker image named alpine_mosquitto was created from alpine with mosquitto installed
* A docker container was started with the name alpine_mosquitto
* The mosquitto process was then kicked off within this docker container to act as the broker for this machine
* We also started the container with the option -p 1883:1883 so that we can have access to the broker from the public ip address

# 

# Links to image files
* https://w251-cloud-object-storage-j3-cos-standard-0js.s3.us-south.cloud-object-storage.appdomain.cloud/face_image_20200125213800.png



## Jetson TX2
### Network Bridge for local mqtt communication
* Created a local network bridge using the following command
  * docker network create --driver bridge w251hw03
* docker_network_start.sh

### Mosquitto Broker
* Created a docker image to run the mosquitto broker with alpine and mosquitto using the following docker file
  * Dockerfile.alpine-mosquitto

### Mosquitto Broker

### Mosquitto Broker
