# import the necessary packages
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

resized = imutils.resize(image, width=100, inter=cv2.INTER_NEAREST)
(b, g, r) = resized[74, 20]
print(str.format("Q1)  r:{}, g:{}, b:{}", r, g, b))

resized = imutils.resize(image, width=image.shape[1]*2, inter=cv2.INTER_CUBIC)
(b, g, r) = resized[367, 170]
print(str.format("Q2)  r:{}, g:{}, b:{}", r, g, b))