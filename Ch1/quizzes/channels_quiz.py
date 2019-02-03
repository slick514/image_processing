# import the necessary packages
import numpy as np
import cv2


image = cv2.imread("florida_trip_small.png")
(B, G, R) = cv2.split(image)

print("{}".format(G[5, 80]))