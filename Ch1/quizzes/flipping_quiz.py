import argparse
import cv2
import imutils

horizontal = 1
vertical = 0
both = -1

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# flip image horizontally
flipped = cv2.flip(image, horizontal)
(b, g, r) = flipped[235, 259]
print(str.format("Q1)  r:{}, g:{}, b:{}", r, g, b))


flipped = cv2.flip(image, horizontal)
rotated = imutils.rotate(flipped, 45)
flipped = cv2.flip(rotated, vertical)
(b, g, r) = flipped[189, 441]
print(str.format("Q1)  r:{}, g:{}, b:{}", r, g, b))