Setup
=====

1.  Create virtual environment with Python 3.6.0

2.  Install dependencies with pip install -r m_requirements.txt

3.  Setup dataset directory

    1.  In the dataset directory, create individual directories, named of the
        person whose images will be trained on (e.g. \\dataset\\bob,
        \\dataset\\amy)

    2.  In each directory, place images of the person, headshots preferably, of
        consecutively numbered values (e.g. 0.jpg, 1.jpg, 2.jpg)

 

Execution
=========

1.  Run python encode_faces.py --dataset dataset --encodings encodings.pickle

    -   \--dataset is the directory containing directories of image files. Each
        directory should be named of the person in the images

    -   \--encodings is the file to output the encoding information of the
        person in the respective directories in --dataset

2.  Run python recognize_faces_image.py --encodings encodings.pickle --image
    examples\\0.jpg

    -   \--encodings points to the encodings file run in step 1

    -   \--image is the file to perform the face recognition on
