Overview
========

Lanuages: Python, with Keras and TensorFlow

This project builds from Adrian Rosebrock, and Dlib’s work in OpenCV, with Python, Keras, and TensorFlow for image recognition to build facial recognition via image encoding. 

 

https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/ 

 

I’ve update the encoding and recognition scripts, and have added the ability to automatically search for and retrieve additional images that may be used for updating the encodings used for recognition. 

 

Setup
=====

1.  Create virtual environment with Python 3.6.0

 

2.  Install dependencies with pip install -r m_requirements.txt

 

3.  Setup dataset directory

 

    1.  In the dataset directory, create individual directories, named of the

        person whose images will be trained on (e.g. \\\\dataset\\\\bob,

        \\\\dataset\\\\amy)

 

    2.  In each directory, place images of the person, headshots preferably, of

        consecutively numbered values (e.g. 0.jpg, 1.jpg, 2.jpg)

 

 

 

Execution
=========

 

1.  Run python encode_faces.py --dataset dataset --encodings encodings.pickle

 

    -   \\--dataset is the directory containing directories of image files. Each

        directory should be named of the person in the images

 

    -   \\--encodings is the file to output the encoding information of the

        person in the respective directories in --dataset

 

2.  Run python recognize_faces_image.py --encodings encodings.pickle --image

    examples\\\\0.jpg

 

    -   \\--encodings points to the encodings file run in step 1

 

    -   \\--image is the file to perform the face recognition on
