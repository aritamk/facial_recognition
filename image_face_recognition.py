import face_recognition
import pickle
import cv2

def read_encodings(encodings_path):
	# load the known faces and embeddings
	print("[INFO] loading encodings...")
	encodings = pickle.loads(open(encodings_path, "rb").read())
	return encodings


def read_image(image_path, get_rgb=False):
	# load the input image and convert it from BGR to RGB
	image = cv2.imread(image_path)

	return image

def image_to_rgb(image):
	rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	return rgb_image


def detect_faces(data_encodings, rgb_image, detection_method, person_names):
	if len(person_names) == 0:
		print("Can't continue. No encodings names provided")
		return None

	# detect the (x, y)-coordinates of the bounding boxes corresponding
	# to each face in the input image, then compute the facial embeddings
	# for each face
	print("recognizing faces")
	boxes = face_recognition.face_locations(rgb_image, model=detection_method)
	print("determining face encodings")
	detected_encodings = face_recognition.face_encodings(rgb_image, boxes)

	matched_people_names = []

	# check encoding from person (data_encodings) against found encoding (encoding)
	for encoding in detected_encodings:
		# attempt to match each face in the input image to our known encodings
		matches = face_recognition.compare_faces(data_encodings, encoding)
		match_person_name = "Unknown"

		# check to see if we have found a match
		if True in matches:
			# find the indices of all matched faces then initialize a
			# dictionary to count the total number of times each face
			# was matched
			matched_indices = [j for (j, b) in enumerate(matches) if b]
			counts = {}

			# map class (person_name) to matches (encoding)
			for j in matched_indices:
				name = person_names[j]
				counts[name] = counts.get(name, 0) + 1

			# then retrieve the class with the most matches
			match_person_name = max(counts, key=counts.get)

		# update the list of names
		matched_people_names.append(match_person_name)

	return boxes, matched_people_names


def draw_boxes(image, boxes, names):
	if image is None or len(names) == 0:
		return None

	# draw bounding box on image with person's name
	for ((top, right, bottom, left), name) in zip(boxes, names):
		# draw the predicted face name on the image
		cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

	return image


def display_image(image):
	image = cv2.resize(image, (960, 540))
	cv2.imshow("Image", image)
	cv2.waitKey(0)

