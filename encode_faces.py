# author: Mark Arita

# USAGE
# python encode_faces.py --dataset dataset --encodings user_encodings.pickle --detection-method "cnn" -name "
# python encode_faces.py --dataset dataset --encodings user_encodings.pickle --detection-method "cnn" -name "alan_grant" --search "C:\\Pictures\\More Jurassic Park Pictures"
	
# import the necessary packages
from imutils import paths
import face_encoding
import argparse
import os

def main():
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--dataset", required=True,
		help="path to input directory of faces + images")
	ap.add_argument("-e", "--encodings", required=True,
		help="path to serialized database of facial encodings")
	ap.add_argument("-d", "--detection-method", type=str, default="cnn",
		help="face detection model to use: either `hog` or `cnn`")
	ap.add_argument("-s", "--search", type=bool, default=False,
		help="search images in subdirectories from current path")
	ap.add_argument("-n", "--name", type=str,
		help="name of the person to identify encodings of")
	ap.add_argument("-a", "--append", type=bool, default=False,
		help="append encodings to s_encodings")
	ap.add_argument("-o", "--saved_encodings", type=str,
		help="file path to saved encodings, for appending new data to")
	args = vars(ap.parse_args())


	# grab the paths to the input images in our dataset
	print("Encoding images")
	if "search" in args and args["search"] == True:
		# This will find all images of the specified person in the provided search tree
		
		# Requires that you have already performed a standard encoding pass with a dataset consisting
		# of images for the person to search for more images of 
		
		import file_retrieval
		extensions = [".jpg", ".png"]

		project_root = os.path.dirname(os.path.realpath(__file__))
		dataset_root = os.path.join(project_root, args["dataset"], args["name"])

		# get all images of person in tree from provided path
		image_paths = file_retrieval.get_all_files(dataset_root, extensions)

		# encode all images in path
		encodings, names = face_encoding.encode_person_images(image_paths, args["detection_method"], args["name"])
	else:
		# encode all images in all subdirectories
		image_paths = list(paths.list_images(args["dataset"]))
		encodings, names = face_encoding.encode_all_images(image_paths, args["detection_method"])

	# save encodings
	face_encoding.save_encodings(encodings, names, args["encodings"])
	print("Done encoding images")

if __name__ == "__main__":
	main()