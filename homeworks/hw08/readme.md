## Homework 8

## Part 1
### In the time allowed, how many images did you annotate?

### Home many instances of the Millennium Falcon did you annotate? How many TIE Fighters?

### Based on this experience, how would you handle the annotation of large image data set?
* It does take a lot of time to mark each object in an image and label them. For large image data set we should either use crowdsourcing, internal team members or outsource to companies that provide this service.

### Think about image augmentation? How would augmentations such as flip, rotation, scale, cropping, and translation effect the annotations?
* Flip could change the boundaries of x and y depending on how symmetrical the image is
* Rotation can change the  

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
