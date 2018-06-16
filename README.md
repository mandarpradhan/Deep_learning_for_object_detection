# Deep_learning_for_object_detection
Description 
===========
This is project Deep_learning_for_object_detection  developed by team Insert_funny_name_here composed of Indumati Sridhar, Mandar Pradhan and Yash Agarwal <br/>
Requirements
============
Install package 'sklearn ' as follow :
$ pip install scikit-learn --user

Install package 'skimage ' as follow :
$ pip install scikit-image --user

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
voc2012test - test ground truth annotations <br/>
voc2007test - train ground truth annotations <br/>


