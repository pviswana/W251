## Homework 8

## Part 1
### In the time allowed, how many images did you annotate?
* I was able to annotate all the 384 files in about 90 mins. 10 files didn't require labeling so a total of 374 labelled files were created.

### Home many instances of the Millennium Falcon did you annotate? How many TIE Fighters?
* Number of Millennium Falcon = 283
* Number of TIE Fighters = 243

### Based on this experience, how would you handle the annotation of large image data set?
* It does take a lot of time to mark each object in an image and label them. For large image data set we should either use crowdsourcing, internal team members or outsource to companies that provide this service.

### Think about image augmentation? How would augmentations such as flip, rotation, scale, cropping, and translation effect the annotations?
* Flip could change the boundaries of x and y depending on how symmetrical the image is
* Rotation can change the orientation and hence the width, height and binding box dimensions can change if the image is not symmetrical. 
* Scale can reduce or increase the dimensions of the annotated image. Also the binding box dimenstions will change.
* Cropping will cause the dimensions of the image to change and sometimes may not be labelled if it is too different from the original one
* Translation depending on the type of translation could change the dimensions or may not be labelled at all.

## Part 2
Describe the following augmentations in your own words
### Flip
* Image can be flipped at the horizontal or vertical axis of the image.

### Rotation
* Image can be rotated by a certain angle

### Scale
* Image can be reduced or increased in size by a certain factor of the original size. Label can be preserved if the size doesn't impact the basic attributes of the original image

### Crop
* A certain section of the image can be used fo fill the entire image and get the effect of cropping such as a face. Depending on the extent of cropping the label may or may not be preserved

### Translation
* Translation is used to translate the original image without changing the overall size and maintaining the basic attributes of the image.

### Noise
* If the image has a lot of information that is not relevant to the definition of the object, we define it as noise and the image is not clear as the original

## Part 3
### Image annotations require the coordinates of the objects and their classes; in your option, what is needed for an audio annotation?
* Timeline of audio components that are being labelled
* Type of audio file being annotated
* Number of channels
* Sampling rate of the audio
* Equalizer settings if applicable
