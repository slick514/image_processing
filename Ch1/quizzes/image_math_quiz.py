# import the necessary packages
import numpy as np
import argparse
import cv2

image = cv2.imread("grand_canyon.png")

np75 = np.ones(image.shape, dtype="uint8")*75
sum = cv2.add(np75, image)
(b, g, r) = sum[152, 61]
print("r:{}, g:{}, b:{}".format(r, g, b))