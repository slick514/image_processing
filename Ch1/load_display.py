
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())


image = cv2.imread(args['image'])
print(str.format("width: {} pixels", image.shape[1]))
print(str.format("height: {} pixels", image.shape[0]))
print(str.format("channels: {}", image.shape[2]))


cv2.imshow("Image", image)
cv2.waitKey(0)


cv2.imwrite("newImage.jpg", image)
