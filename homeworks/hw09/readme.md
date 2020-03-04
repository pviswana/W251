### TensorBoard output

![TensorBoard Output](https://github.com/pviswana/W251/blob/master/homeworks/hw09/TensorBoardOutput.png)


### How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while)
* It took 25 hours to complete the training run with max steps = 50K

### Do you think your model is fully trained? How can you tell?
* The training did completed the max steps of 50K, but I think the model could be further trained to reduce the loss. 
* The loss function was not fully converged, so there was more room for improvement.

### Were you overfitting?
* Based on the graphs it doesn't look like we are overfitting yet. It is possible that if we run the training model for more number of steps the loss may reduce more and possibly cause overfitting.

### Were your GPUs fully utilized?
* The GPUs were 100% utilized as seen below

![GPU Utilization](https://github.com/pviswana/W251/blob/master/homeworks/hw09/GPUUsage.png)

### Did you monitor network traffic (hint: apt install nmon ) ? Was network the bottleneck?
* I did monitor network traffic
![Network monitoring](https://github.com/pviswana/W251/blob/master/homeworks/hw09/NetworkMonitoring.png)

### Take a look at the plot of the learning rate and then check the config file. Can you explan this setting?
* The learning rate policy has the warmup_steps value set to 8000. So as we can see in the plot for the first 8000 steps it uses a small learning rate value and then starts to use the set value of 2.0 for the learning rate.

### How big was your training set (mb)? How many training lines did it contain?
* train.en -> 636.46 mb
  * Number of lines = 4562102

* train.de -> 710.26 mb
  * Number of lines = 4562102

### What are the files that a TF checkpoint is comprised of?
* Checkpoint data file
* Index file
* Meta data file

### How big is your resulting model checkpoint (mb)?
* Resulting model checkpoint size = 852.27 mb

### Remember the definition of a "step". How long did an average step take?
* Avg time per step: 1.798s

### How does that correlate with the observed network utilization between nodes?
