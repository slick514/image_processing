# import the necessary packages

import argparse
import imutils
import cv2

# All of these answers ended up being wrong.  Don't care

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])

(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)
rotated = imutils.rotate(image, 30)
(r, g, b) = rotated[254, 335]
print(str.format("Q1: {}, {}, {}", r, g, b))

rotated = imutils.rotate(image, -110)
(r, g, b) = rotated[136, 312]
print(str.format("Q2: {}, {}, {}", r, g, b))

rotated = imutils.rotate(image, -88, (50, 50))
(r, g, b) = rotated[10, 10]
print(str.format("Q2: {}, {}, {}", r, g, b))