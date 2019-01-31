import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

(b, g, r) = image[0, 0]

# print("width: {w} pixels".format(w=image.shape[1]))
# print("height: {h}  pixels".format(h=image.shape[0]))
print(str.format("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}", r, g, b))



#Make the pixel red
image[0, 0] = (0, 0, 255)

(b, g, r) = image[0, 0]
print(str.format("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}", r, g, b))

#calculate center point of image
(cX, cY) = (w // 2, h // 2)

#let's just show the corners of the image
tl = image[0:cY, 0:cX]
cv2.imshow("Top-Left", tl)

tr = image[0:cY, cX:w]
cv2.imshow("Top-Right", tr)

bl = image[cY:h, 0:cX]
cv2.imshow("Bottom-Left", bl)

br = image[cY:h, cX:w]
cv2.imshow("Botton-Right", br)

image[0:cY, 0:cX] = (0, 255, 0)
cv2.imshow("Updated", image)

cv2.waitKey(0)