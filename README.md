# Road Sign Classifier

Given a labelled data set of German road signs, build a deep learning traffic sign classifier in TensorFlow. 

![alt text][image16]

The major steps in this project are the following:

* Load the data set.
* Explore, summarize and visualize the data set.
* Design, train and test a model architecture.
* Use the model to make predictions on new images.
* Analyze the softmax probabilities of the new images.
* Summarize the results with a written report.

## Getting Started

### Prerequisites

Imported packages include:

```
Python
TensorFlow
Keras
skimage
```

### Installing

No install is required --- simply clone this project from GitHub:

```
git clone https://github.com/jimwatt/P2-trafficsigns.git
```

## Running the Code

* The main python script is a Jupyter Notebook called Traffic\_Sign\_Classifier.ipynb
* Just start by running the Jupyter Notebook, and then experimenting.
* Training will be faster if this notebook is run on a GPU (through Amazon Web Services, for example).




## Authors

* **James Watt**

<!--## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details-->

## Acknowledgments
This project is a submission to the Udacity Self-Driving Car nanodegree:

* <https://github.com/udacity/CarND-Traffic-Sign-Classifier-Project>

The deep network architecture is loosely based on the LeCun network of
Pierre Sermanet and Yann LeCun: __Traffic Sign Recognition with Multi-Scale Convolutional Networks, Proceedings of International Joint Conference on Neural Networks (IJCNN'11), 2011__.



# **Traffic Sign Recognition** 

## Writeup

------

**Build a Traffic Sign Recognition Project**

Given a labelled data set of German road signs, build a deep learning traffic sign classifier.  
The major steps in this project are the following:

- Load the data set.
- Explore, summarize and visualize the data set.
- Design, train and test a model architecture.
- Use the model to make predictions on new images.
- Analyze the softmax probabilities of the new images.
- Summarize the results with a written report.

[//]: #	"Image References"
[image1]: ./figs/histogram.jpg	"Visualization"
[image2]: ./examples/grayscale.jpg	"Grayscaling"
[image3]: ./examples/flip.jpg	"Symmetry"
[image4]: ./examples/sym.jpg	"Symmetry"
[image5]: ./examples/augment.png	"Keras"
[image6]: ./data/signs/resized/sign0.png	"Traffic Sign 1"
[image7]: ./data/signs/resized/sign1.png	"Traffic Sign 2"
[image8]: ./data/signs/resized/sign2.png	"Traffic Sign 3"
[image9]: ./data/signs/resized/sign3.png	"Traffic Sign 4"
[image10]: ./data/signs/resized/sign4.png	"Traffic Sign 5"
[image11]: ./data/signs/resized/sign5.png	"Traffic Sign 6"
[image12]: ./data/signs/resized/sign6.png	"Traffic Sign 7"
[image13]: ./data/signs/resized/sign7.png	"Traffic Sign 8"
[image14]: ./data/signs/resized/sign8.png	"Traffic Sign 9"
[image15]: ./data/signs/resized/sign9.png	"Traffic Sign 10"
[image16]: ./examples/scores.png	"Probabilities"
[image17]: ./examples/features.png	"Features"

## Rubric Points

### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/481/view) individually and describe how I addressed each point in my implementation.  

------

### Writeup

You're reading it! and here is a link to my [project code](https://github.com/jimwatt/P2-trafficsigns.git) on GitHub.

### Data Set Summary & Exploration

#### 1. A basic summary of the data set. 

I used python and numpy to calculate summary statistics of the traffic
signs data set:

- The size of training set is 34,799.
- The size of the validation set is 4,410.
- The size of test set is 12,630.
- The shape of a traffic sign image is (32, 32, 3).
- The number of unique classes/labels in the data set is 43.

#### 2. Include an exploratory visualization of the dataset.

Here is an exploratory visualization of the data set. It is a histogram showing the distribution of images over the classes.  The distribution is not uniform.

![alt text][image1]

### Design and Test a Model Architecture

- I used conversion to grayscale, as I did not notice any appreciable improvement when using all three original channels.
- The conversion to grayscale is just a simple average over the channels.
- Each image was also normalized to ensure that it has zero mean across the pixel values with standard deviation of unity.
- Normalization helps improve conditioning and scaling during training of weights in the network, and ensures that very underexposed images are put on equal footing with bright images.

![alt text][image2]

I decided to generate additional data because who doesn't want more data? 

To add more data to the the data set, I used the following techniques:

- First, I exploited symmetry to obtain more images.  Several of the signs are symmetric about the vertical axis. For example, given the image on the left, we can easily generate the image on the right. 

![alt text][image3]

- Second, I exploted symmetry again between pairs of classes.  For example, the "Keep Right" can easily be used to generate another image in the "Keep Left" category.

![alt text][image4]

- Finally, I also used the Keras ImageDataGenerator() class for generation of additional images by applying rotations, shifts, zooming, and shearing to the images in the original dataset.

During training, I used the ImageDataGenerator.flow() method to generate new data "inline" as the training epochs proceed.  Left is an original image, and right is the image generated by ImageDataGenerator.flow().

![alt text][image5]

#### 2. Final model architecture

I started with the LeCun network from the tutorial.  I then experimented with a few architectural modifications.  Here is what I observed:

- Adding drop-out regularization improved performance.
- Adding additional layers did not seem to help appreciably, at least not for the small number of epochs (15) I was using to keep run time low.
- Drop-out performed better than pooling layers so I removed pooling layers.
- The most important thing I learned is that Deep Learning is not yet a science.  Any field where progress is made by intuition, recipes, and considering what worked and didn't work last time, rather than principled analysis of performance guarantees is still an art more than a disciplined approach.  We tell ourselves stories about regularization and universality to make ourselves feel better, but really we are just blindly hacking away at a system with a bag of tricks that we don't really understand.

My final model consisted of the following layers:

|      Layer      |                 Description                 |
| :-------------: | :-----------------------------------------: |
|      Input      |           32x32x1 Grayscale image           |
| Convolution 5x5 | 1x1 stride, valid padding, outputs 28x28x6  |
|      RELU       |                                             |
|    Drop out     |           keep probability = 0.5            |
| Convolution 5x5 | 1x1 stride, valid padding, outputs 24x24x16 |
|      RELU       |                                             |

| Drop out	      	| keep probability = 0.5
| Fully connected		| Input 9216, Output 120      									|
| RELU					|												|
| Drop out	      	| keep probability = 0.5 
| Fully connected		| Input 120, Output 84 
| RELU		
| Fully connected		| Input 84, Output 43			|
| Softmax				|	Input 43  Output 43        									|
​				



#### 3. Describe how you trained your model. The discussion can include the type of optimizer, the batch size, number of epochs and any hyperparameters such as learning rate.

To train the model, I used the AdamOptimizer in TensorFlow.  I trained the model on the Amazon Web Services cloud-based GPU.  As I experimented with different architectures, I tried to follow these rules:

- Beware of over-fitting.  Introduce more data and regularization (drop-out) if over-fitting appears to be an issue.
- I did not pursue long training runs with many epochs.  Generally, I would not let a training run continue if performance plateaued or worsened.

#### 4. Describe the approach taken for finding a solution and getting the validation set accuracy to be at least 0.93. Include in the discussion the results on the training, validation and test sets and where in the code these were calculated. Your approach may have been an iterative process, in which case, outline the steps you took to get to the final solution and why you chose those steps. Perhaps your solution involved an already well known implementation or architecture. In this case, discuss why you think the architecture is suitable for the current problem.

I started withe the LeCun network as a baseline which achieved an accuracy performance of about 0.87.  I found through experimentation that performance improved when I:

- included normalization of the images,
- added regularization via dropout,
- added more data through image generation.

If I were to do this project again, I would try to use image augmentation to provide a more uniform distribution of labelled sign data.

My final model results were:

- training set accuracy of 0.991
- validation set accuracy of 0.963
- test set accuracy of 0.952

### Test a Model on New Images

#### 1. Choose five German traffic signs found on the web and provide them in the report. For each image, discuss what quality or qualities might be difficult to classify.

Here are ten German traffic signs that I found on the web:

![alt text][image6] ![alt text][image7] 
![alt text][image8] ![alt text][image9] 
![alt text][image10] ![alt text][image11]
![alt text][image12] ![alt text][image13]
![alt text][image14] ![alt text][image15]

I expect good classification performance on these images because they are all well-resolved images in good lighting.  There are no occlusions, shadows, glare, etc.  (It was quite difficult to find poor quality images of signs).

#### 2. Discuss the model's predictions on these new traffic signs and compare the results to predicting on the test set. At a minimum, discuss what the predictions were, the accuracy on these new predictions, and compare the accuracy to the accuracy on the test set (OPTIONAL: Discuss the results in more detail as described in the "Stand Out Suggestions" part of the rubric).

Here are the results of the prediction:

| Image			        |     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| Stop       		| Stop    									
| Yield					| Yield											|
| 30 km/h	      		| 30 km/h				 				|
| Ahead Only			| Ahead Only 
| Bumpy Road      	| Bumpy Road	
| 60 km/h	      		| 60 km/h		
| Caution				| Caution
| 80 km/h	      		| 80 km/h	
| No Passing	      		| No Passing
| Right-of-way		| Right-of-way	

The model correctly classified 10 of the 10 traffic signs, which gives an accuracy of 100%. This compares favorably to the accuracy on the test set of 95.2 %.

The model was somewhat uncertain when classifying the 60 km/hr sign --- confusing it with the 80 km/hr sign.

#### 3. Describe how certain the model is when predicting on each of the five new images by looking at the softmax probabilities for each prediction. Provide the top 5 softmax probabilities for each image along with the sign type of each probability. (OPTIONAL: as described in the "Stand Out Suggestions" part of the rubric, visualizations can also be provided such as bar charts)

The results of the softmax probability study are shown in the next figure:

![alt text][image16]



### Visualizing the Neural Network

#### 1. Discuss the visual output of your trained network's feature maps. What characteristics did the neural network use to make classifications?

Visualization of the features (at the layer of the first convolutional network) stimulated by each of the 10 extra images is shown below.  Strikingly, the network captures the shape and important edges of each sign. To some degree, this layer is also trying to capture the presence of lettering, although I found that lettering was more strongly visible in the second conolutional layer (not shown here).

![alt text][image17]

