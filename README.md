
# YOLOv8 Segmentation Model

This project aims to develop a custom segmentation model using YOLOv8 to identify and segment objects in images from the DeepBee dataset. The process involved downloading images, annotating them, and training a YOLOv8 model for segmentation tasks.

<h2> Dataset</h2>
The dataset was sourced from the DeepBee repository, specifically designed for bee segmentation tasks. The images in this dataset are annotated with bounding boxes labeling different elements such as 'eggs' and 'larvae' within the frames.

## Background
YOLOv8 is an advanced object detection and segmentation model, offering high accuracy and efficiency. This project uses YOLOv8 to leverage its capabilities in segmenting objects from the DeepBee dataset, which provides a valuable testbed for such applications.
## Objectives
Dataset Acquisition: Download images from provided links.
Annotation: Annotate images using Roboflow in YOLOv8 format.
Model Training: Train a YOLOv8 model for object segmentation.
Validation and Evaluation: Assess model performance and accuracy.
## Dataset
Source: DeepBee dataset<br>
Files:
images.csv: Contains image names and download links.<br>
labels.csv: Contains image annotations.
Process:<br>
Download images using links from images.csv.<br>
Annotate images using Roboflow.


## Acknowledgements

 - [Deep Bee Dataset](https://github.com/avsthiago/deepbee-source/tree/release-0.1/src/data/resources)
 - [Github](https://github.com/VedantDeore/BeeFrameSegmentation)

## Authors

- [@VedantDeore](https://github.com/VedantDeore)
- [@SahilDeogade](https://github.com/Sahildeogade03)
- [@DarshanBiradar](https://github.com/darshannbiradar)
- [@VishalBokare](https://github.com/Vishalbokare45)
- [@RajasBhosale](https://github.com)





## Badges



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



## Documentation

[Project Report](https://docs.google.com/document/d/1PrZ0mt_gCCAt2bUbitIx18vRP6i9UCzT/edit?usp=drive_link&ouid=113719066612185762728&rtpof=true&sd=true)


## Features
1. Bee Region Segmentation: Utilizes a deep learning-based segmentation model to accurately identify and isolate the region of bees in images, excluding non-relevant elements.

2. DeepBee Dataset: Leverages the DeepBee dataset, specifically designed for bee segmentation tasks, including annotated images with bounding boxes for eggs, larvae, and other features.

3. Advanced Data Preprocessing: Incorporates data preprocessing steps such as bounding box conversion and data augmentation techniques (random rotation, flipping, scaling) to enhance model robustness and performance.

4. Convolutional Neural Network (CNN) Architecture: Employs a CNN architecture for effective spatial feature extraction, suitable for segmentation tasks in image processing.

5. Performance Evaluation: Assesses model accuracy and efficiency using key metrics like mean Average Precision (mAP) and F1-score, providing a comprehensive analysis of segmentation performance.

6. Optimization Techniques: Implements optimization strategies including hyperparameter tuning, learning rate adjustments, and early stopping to improve model performance.

7. Collaborative Development: Utilizes GitHub for version control and team collaboration, ensuring seamless integration of code and documentation among team members.
 
8. Scalable and Extensible: The model is designed to be scalable and adaptable for further development, allowing for integration with additional datasets and extended functionalities.



## Screenshots
![image 1](https://github.com/user-attachments/assets/8802d970-7ed7-42c2-a64e-1367cbcbf19f)

![image 2](https://github.com/user-attachments/assets/caf6774a-ae50-41ac-b9c2-3c3d92e0ef11)
![image 3](https://github.com/user-attachments/assets/d6c1b3a4-d654-408b-af24-49a6daf39eff)


## Optimizations

Various techniques, such as adjusting learning rates and implementing early stopping, were explored to enhance the model's performance. These optimizations led to marginal improvements in the model's accuracy and efficiency.


## Related

Here are some related projects

[Project 1](https://github.com/matiassingers/awesome-readme)

