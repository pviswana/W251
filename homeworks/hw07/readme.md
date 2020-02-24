## Output files link

https://w251-cloud-object-storage-j3-cos-standard-0js.s3.us-south.cloud-object-storage.appdomain.cloud/face_image_20200224082239.png

https://w251-cloud-object-storage-j3-cos-standard-0js.s3.us-south.cloud-object-storage.appdomain.cloud/face_image_20200224082238.png

### Describe your solution in detail. What neural network did you use? What dataset was it trained on? What accuracy does it achieve?


### Does it achieve reasonable accuracy in your empirical tests? Would you use this solution to develop a robust, production-grade system?
It seems to achieve reasonable accuracy in the empirical tests. I might add my own layer of training to the pre-trained model and see if I can get better accuracy for a production environment.

### What framerate does this method achieve on the Jetson? Where is the bottleneck?
We are 

### Which is a better quality detector: the OpenCV or yours?
I could not see much of a quality difference between OpenCV and the tensorflow model we used for this homework.
