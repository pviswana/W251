sudo docker run --rm --name mosquitto --network w251hw03 -v "$PWD":/hw03 -p 1883:1883 -ti alpine_mosquitto sh
