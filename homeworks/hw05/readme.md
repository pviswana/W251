Homework 05

### What is TensorFlow? Which company is the leading contributor to TensorFlow?
* TensorFlow is an end-to-end open source machine learning platform. Google is the leading contributor to TensorFlow

### What is TensorRT? How is it different from TensorFlow?
* TensorRT is an SDK provided by NVIDIA for high performance deep learning inference. It includes a deep learning inference optimizer and runtime that delivers low latency and high-throughput for deep learning inference applications.
* TensorRT can be combined with TensorFlow where TensorFlow can create the deep learning models and TensorRT can be used for hig performance deep learning inference

### What is ImageNet? How many images does it contain? How many classes?
* ImageNet is an image database organized according to the WordNet hierarchy in which each node of the hierarchy is depicted by hundreds and thousands of images
* Currently there are about 500 images per node on an average. The total number of images is around 14 million.
* There are about 27 high level classes and 21,841 sub classes.

### Please research and explain the differences between MobileNet and GoogleNet (Inception) architectures.
* GoogleNet is a pretrained convolutional neural network that is 22 layers deep. You can load a network either trained on ImageNet or Places365 data sets. 
* MobileNet is an architecture which is more suitable for mobile and embedded based vision applications where there is lack of compute power.

### In your own words, what is a bottleneck?
* A bottleneck in a neural network is a layer with less neurons than the layer above or below it. This layer encourages the network to compress feature representations to best fit in the available space, and get the best loss during training.It can be used to obtain a representation of the input with reduced dimensionality.

### How is a bottleneck different from the concept of layer freezing?
* Layer freezing implies that the layer weights of a trained model are not changed when they are used in a subsequent downstream task. They remain frozen. When backprop is done during training these layer weights are untouched.
Bottleneck on the other hand is used to reduce the dimensionality of the input during the training process by reducing the number of neurons for that layer.

### In part one this lab, you trained the last layer (all the previous layers retain their already-trained state). Explain how the lab used the previous layers (where did they come from? how were they used in the process?)

### Why is the batch size important? What happens if you try running with a batch size of 32? What about a batch size of 4?

### Find another image classification feature vector from tfhub.dev and rerun the notebook. Which one did you pick and what changes, if any did you need to make?

### How long did the training take in part 2?

### In part 2, you can also specifiy the learning rate using the flag --learning_rate. How does a low --learning_rate (part 2, step 4) value (like 0.001) affect the precision? How much longer does training take?

### How about a --learning_rate (part 2, step 4) of 1.0? Is the precision still good enough?

### For part 2, step 5, How accurate was your model? Were you able to train it using a few images, or did you need a lot?
