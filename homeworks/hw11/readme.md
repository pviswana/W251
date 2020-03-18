## Configurations

### Baseline Configuration
* Threshold = 3000
* Number of iterations = 50000
* Batch Size = 20
* Epochs = 10 
* Optimizer = adam
* Hidden Layer Activation = sigmoid
* Number of hidden layers = 1
* Number of neurons in input layer = 32
* Number of neurons in hidden layers = 16
* Loss method = mean_squared_error

* With the baseline configuration shown above the processing was slow and the accuracy of landing was not good
* Sample video
https://w251-cloud-object-storage-j3-cos-standard-0js.s3.us-south.cloud-object-storage.appdomain.cloud/basic_config_video.mp4

### Configuration with Activation Method = Relu for the hidden layer
* Threshold = 3000
* Number of iterations = 50000
* Batch Size = 20
* Epochs = 10 
* Optimizer = adam
* **Hidden Layer Activation = relu**
* Number of hidden layers = 1
* Number of neurons in input layer = 32
* Number of neurons in hidden layers = 16
* Loss method = mean_squared_error

* The changes from baseline was that the hidden layer activation was modified from `sigmoid` to `relu`

Sigmoid transforms the input value to an output between 0.0 and 1.0 and is also non-linear in nature. This allows us to stack the layers since the combinations of this function is also nonlinear. One of the issues with `sigmoid` is that towards either end of the function the Y values respond very less to changes in X. So the gradient at that region is going to be small causing the issue of `vanishing gradients`

On the other hand `relu` function 
  * A(x) = max(0,x)
  
`ReLu`is more efficient since it outputs 0 for negative values of x which implies fewer neurons are firing and the network is lighter (hence faster). `ReLu` also doesn't have the vanishing gradient problem since during back propagation it doesn't pass gradients that are getting smaller and smaller instead they stay the same.
* Sample Video
* https://w251-cloud-object-storage-j3-cos-standard-0js.s3.us-south.cloud-object-storage.appdomain.cloud/relu_video.mp4

### Configuration with Activation Method = Relu for the hidden layer + an additional hidden layer 
* Threshold = 3000
* Number of iterations = 50000
* Batch Size = 20
* Epochs = 10 
* Optimizer = adam
* **Hidden Layer Activation = relu**
* **Number of hidden layers = 2**
* Number of neurons in input layer = 32
* Number of neurons in hidden layers = 16
* Loss method = mean_squared_erro

