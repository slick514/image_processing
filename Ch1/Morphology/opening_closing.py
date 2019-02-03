# opening = an erosion followed by a dilation
# closing = a dilation followed by an erosion

# import the necessary packages
import argparse
import cv2

# load the image and convert it to grayscale
image = cv2.imread("../../images/pyimagesearch_logo_noise.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original w/noise", image)
kernelSizes = [(3, 3), (5, 5), (7, 7)]

# loop over the kernels and apply an "opening" operation to the image
for kernelSize in kernelSizes:
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
	cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)

cv2.waitKey(0)

# load the image and convert it to grayscale
image = cv2.imread("../../images/pyimagesearch_logo.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", image)

# loop over the kernels and apply a "closing" operation to the image
for kernelSize in kernelSizes:
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
	cv2.imshow("Closing: ({}, {})".format(kernelSize[0], kernelSize[1]), closing)

cv2.waitKey(0)