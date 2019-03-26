# author: Mark Arita
# USAGE
# python .\update_user_images.py --encodings encodings.pickle --person "alan_grant" --search-path "C:\\Photos\\January"

# Searches in the provided path for more images of the specified person 

import os
import file_retrieval
import argparse
import image_face_recognition as ifr


def setup():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--detection_method", required=False, type=str, default="cnn",
                    help="Detection method, 'hog', or 'cnn'")
    ap.add_argument("-e", "--encodings", required=True, type=str,
                    help="Image encodings information file")
    ap.add_argument("-p", "--person", required=True, type=str,
                    help="Person to search for")
    ap.add_argument("-sp", "--search_path", required=True, type=str,
                    help="Tree root to search for user images")
    args = vars(ap.parse_args())
	
    project_root = os.path.dirname(os.path.realpath(__file__))
    training_root = os.path.join(project_root, "training_data")
    search_path = os.path.join(project_root, args["search_path"])

    print("Project root: ", project_root)
    print("Training data path: ", training_root)
    print("Searching images from: ", search_path)

    # get all child files from search tree
    exts = [".jpg", ".png"]
    image_files = file_retrieval.get_all_files(search_path, exts)
    if image_files is None:
        print("No files found")
        return None

    args["image_files"] = image_files
    args["dest_path"] = training_root

    return args


def get_user_images(files, user_name, encodings_file, detection_method):
    if len(files) == 0 or user_name == "":
        return None

    user_images = []

	# check all images against encodings for specified person and 
	# track which images the person is in 
    for file in files:
        user_image = ""

        print("Searching image: ", file)
        # read in image
        image = ifr.read_image(file)
        rgb_image = ifr.image_to_rgb(image)

        encodings_data = ifr.read_encodings(encodings_file)

        # perform facial recognition
        boxes, names = ifr.detect_faces(encodings_data["encodings"], rgb_image, detection_method, encodings_data["names"])

        # save image if person is in it
        if user_name in names:
            user_images.append(user_image)

    return user_images


def copy_images(source_files, dest_root, name):

	# todo: copy images from source to dest with file name as iterative counter
	for i in range(source_files):
        print("Identified {} in file: {}".format(name, source_files[i]))
		
    print("done")


def main():
    # get paths to all image files
    args = setup()

    # detect specified person in all files
    detected_images = get_user_images(args["image_files"], args["person"], args["encodings"], args["detection_method"])

    # copy all detected images to location
    copy_images(detected_images, args["dest_path"], args["person"])

if __name__ == "__main__":
    main()
