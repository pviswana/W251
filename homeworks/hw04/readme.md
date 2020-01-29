### Name all the layers in the Network
* Input layer that declares the size of input volume and must be the first layer of the network. 
The size is defined using sx, sy and depth values.
* The convolution layer that specifies the filter size `sx`, the filter size `filters`, the number of filters 
and the stride at which they are applied. You can also specify the pad size to pad the input by some amount of pixels to zero. You can also set the activation parameter. 
In this case it is set to `relu`
* The pool layer performs max pooling. It has the same paramters as the convolutional layer except the activation.
* The last layer is the the Classifier layer. We are using `softmax`to classify into 10 classes. The sum of the probabilities of these different classes should add up to 1.

### Experiment with number and size of filters in each layer. Does it improve accuracy

### Remove the pooling layers. Does it impact the accuracy?

### Add one more conv layer. Does it help with accuracy?

### Increase the batch size. What impact does it have?

### What is the best accuracy you can achieve? Are you over 99%? 99.5%?
