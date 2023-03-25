# End-to-End-Distributed-ANPR
The proposed system is intended to employ ANPR solution in a distributed architecture for improved performance, and scalability. 

## System Uses
The developed system uses three stage machine learning models, with YOLOv7 based object detection, SRGAN based Image Upscaling and Optical charecter recognition for segmentation and labelling of license plate.

## To build this project

 * Start with building YOLOv7 by cloning from the repository and training on Custom license plate detection dataset for custom license plate object detection.
 * Then clone the repository for SRGAN and build the code to svale the resolution of cropped images
 * Finally build deep learning benchmark by clovaai to build the OCR part of the project with ResNet as feature extraction and BiLSTM sequence modelling. 
