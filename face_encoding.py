# import the necessary packages
from imutils import paths
import face_recognition
import pickle
import cv2
import os

def encode_person_images(image_paths, detection_method, name):
	if len(image_paths) == 0:
		print("Can't continue. No image paths provided!")
		return None

	if name is None:
		print("Can't continue. No name provided!")
		return None

	person_encodings = []
	primary_names = [name]

	print("Encoding images for single person: ", name)
	print("Using detection method: {} for {}".format(detection_method, name))

	# loop over the image paths
	for image_path in image_paths:
		print("[INFO] processing image: ", image_path)

		# load the input image and convert it from RGB (OpenCV ordering)
		# to dlib ordering (RGB)
		image = cv2.imread(image_path)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detect the (x, y)-coordinates of the bounding boxes
		# corresponding to each face in the input image
		boxes = face_recognition.face_locations(rgb, model=detection_method)

		# compute the facial embedding for the face
		image_encodings = face_recognition.face_encodings(rgb, boxes)

		# append encodings
		for encoding in image_encodings:
			# add each encoding + name to our set of known names and encodings
			person_encodings.append(encoding) # encodings / parameters for image
			primary_names.append(name)		  # need to provide name (class) for each image

	return person_encodings, primary_names


def encode_all_images(image_paths, detection_method):
	# initialize the list of known encodings and known names
	knownEncodings = []
	knownNames = []

	print("Encoding all images in subdirectories")
	print("Using detection method: ", detection_method)

	# loop over the image paths
	for (i, imagePath) in enumerate(image_paths):
		# extract the person name from the image path
		print("[INFO] processing image {}/{}".format(i + 1, len(image_paths)))
		name = imagePath.split(os.path.sep)[-2]

		# load the input image and convert it from RGB (OpenCV ordering)
		# to dlib ordering (RGB)
		image = cv2.imread(imagePath)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detect the (x, y)-coordinates of the bounding boxes
		# corresponding to each face in the input image
		boxes = face_recognition.face_locations(rgb, model=detection_method)

		# compute the facial embedding for the face
		encodings = face_recognition.face_encodings(rgb, boxes)

		# loop over the encodings
		for encoding in encodings:
			# add each encoding + name to our set of known names and
			# encodings
			knownEncodings.append(encoding)
			knownNames.append(name)
	
	return knownEncodings, knownNames

def save_encodings(encodings, names, encodings_file):
	# dump the facial encodings + names to disk
	print("[INFO] serializing encodings...")
	data = {"encodings": encodings, "names": names}
	f = open(encodings_file, "wb")
	f.write(pickle.dumps(data))
	f.close()
