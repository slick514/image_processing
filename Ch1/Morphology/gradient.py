# import the necessary packages
import argparse
import cv2

# load the image and convert it to grayscale
image = cv2.imread("../../images/pyimagesearch_logo.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", image)

kernelSizes = [(3, 3), (5, 5), (7, 7)]

# loop over the kernels and apply a "morphological gradient" operation
# to the image
for kernelSize in kernelSizes:
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
	cv2.imshow("Gradient: ({}, {})".format(kernelSize[0], kernelSize[1]), gradient)

cv2.waitKey(0)