xhost local:root
sudo docker 	run \
	-e DISPLAY=$DISPLAY \
	--rm \
	--env QT_X11_NO_MITSHM=1 \
	--name face_app_jtx2 \
	--privileged \
	--network w251hw03 \
	-v "$PWD":/HW03 \
	-v /tmp:/tmp \
	-ti ubuntu_opencv_mqtt_tx2 bash
