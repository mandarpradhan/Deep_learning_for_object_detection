# Deep_learning_for_object_detection
Description 
===========
This is project Deep_learning_for_object_detection  developed by team Insert_funny_name_here composed of Indumati Sridhar, Mandar Pradhan and Yash Agarwal <br/>
Requirements
============
- Please download images of the VOC 2012 data from http://host.robots.ox.ac.uk/pascal/VOC/voc2012/#devkit and give it the path 'VOC_Datasets/VOC_2012_training/VOC2012/JPEGImages/' relative to the main directory <br/>
Please download images of the VOC 2007 data from http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar and give it the path 'VOC_Datasets/VOC_2007_testing/VOCdevkit/VOC2007/JPEGImages/' relative to the main directory <br/>
use tar -xvf 'filename' to untar <br/>
Install package 'sklearn ' as follow :
$ pip install scikit-learn --user

Install package 'skimage ' as follow :
$ pip install scikit-image --user

Install package 'cv2 ' as follow :
$ pip install opencv-python --user

Install package 'tqdm ' as follow :
$ pip install tqdm --user

Code organization
=================
Demo.ipynb -- Run this to see a demo of the object detector <br/>
PLease download the file 'best.pth' to this same directory as the one containing Demo.ipynb to run the Demonstration.
path to download best.pth ==> https://drive.google.com/file/d/1BIAHNjsrb4KWQNQnWOADgrHmG-xKRgR5/view?usp=sharing <br/>
Our_VGG16.py - contains our VGG base architecture <br/>
Training.ipynb - Trains the model <br/>
predict.py - To run on the test data to get bounding boxes as in figure 9-15 <br/>
yolo_loss.py - It is the separate python file to deal with loss function for the model <br/>
CONFIG.py -- contains global variables and paths to change <br/>

[Demo_image01/2/3/4] -- Input images of demo.ipynb <br/>
voc2012test - Training ground truth annotations <br/>
voc2007test - Testing ground truth annotations <br/>


