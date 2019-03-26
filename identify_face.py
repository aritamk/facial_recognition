# USAGE

# python recognize_faces_image.py --encodings encodings.pickle --image examples/example_01.png 

# Uses the encodings provided from encode_faces.py on the provided test image 
# to determine whether it's the same person or not

# import the necessary packages
import argparse
import image_face_recognition as ifr

def main():
	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-e", "--encodings", required=True,
					help="path to serialized db of facial encodings")
	ap.add_argument("-i", "--image", required=True,
					help="path to input image")
	ap.add_argument("-d", "--detection-method", type=str, default="cnn",
					help="face detection model to use: either `hog` or `cnn`")
	args = vars(ap.parse_args())

	encodings = ifr.read_encodings(args["encodings"])
	image = ifr.read_image(args["image"])
	rgb_image = ifr.image_to_rgb(image)
	images = [image]
	boxes, names = ifr.detect_faces(encodings["encodings"], rgb_image, args["detection-method"], encodings["names"])

	for i in range(len(images)):
		print("Detected {} in image {}".format(names[i], args["image"]))

	image = ifr.draw_boxes(image, boxes, names)
	ifr.display_image(image)


if __name__ == "__main__":
	main()