### Name all the layers in the Network
* Input layer that declares the size of input volume and must be the first layer of the network. 
The size is defined using sx, sy and depth values.
* The convolution layer that specifies the filter size `sx`, the number of filters `filters`,  
and the stride at which they are applied. You can also specify the pad size to pad the input by some amount of pixels to zero. You can also set the activation parameter, in this case it is set to `relu`
* The pool layer performs max pooling. It has the same paramters as the convolutional layer except the activation.
* The last layer is the the Classifier layer. We are using `softmax`to classify into 10 classes. The sum of the probabilities of these different classes should add up to 1.

### Initial State
* The initial values for training accuracy was around 99%
* The initial values for validation accuracy was around 96%

### Experiment with number and size of filters in each layer. Does it improve accuracy
* When I increase the size of the filters the training accuracy and the validation accuracy went down. It makes sense since we are now detecting broader sections of the original image to form the complete picture
* When I increased the number of filters, the process got slower and at 10K examples the training accuracy was close to 99% and the validation one was at 94%

### Remove the pooling layers. Does it impact the accuracy?
By removing the pooling layers the training accuracy goes up to almost 100% and the validation accuracy was at 99%. Both seem to go up. The intuition here is that by removing the pooling we have left all the dimensions of the conv layer and hence it seems to more accurately train the model.

### Add one more conv layer. Does it help with accuracy?
Adding one more conv layer improved the training accuracy to 99% but the validation accuracy reduced a little bit. Could be overfitting the model

### Increase the batch size. What impact does it have?
Increasing the batch size to 40 made the training accuracy 99% while the validation accuracy stayed at 94%. This could indicate a case of overfit to the training data.

### What is the best accuracy you can achieve? Are you over 99%? 99.5%?
The best accuracy achieved was 99% and once in a while the training frequency jumped to 100%
