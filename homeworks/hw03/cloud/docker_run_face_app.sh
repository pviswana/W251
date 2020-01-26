#!/bin/bash
xhost+

docker 	run \
	--env="DISPLAY" \
	--name face_app_cloud \
	--privileged \
	--network w251hw03 \
	-v "$PWD":/HW03 \
	-ti face-app-ubuntu-mqtt-py bash
