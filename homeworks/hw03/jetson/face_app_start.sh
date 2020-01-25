#!/bin/bash
xhost + local:root

docker 	run \
	--env="DISPLAY" \
	--name face_app_jtx2 \
	--privileged \
	--network w251hw03 \
	-v "$PWD":/HW03 \
	-ti ubuntu_opencv_mqtt_tx2 bash
