import cv2

# load the image and show it
image = cv2.imread("florida_trip.png")

i = image[173:235, 13:81]
cv2.imshow("3", i)

i = image[124:212, 225:380]
cv2.imshow("4", i)

i = image[90:450, 0:290]
cv2.imshow("2", i)

i = image[85:250, 85:220]
cv2.imshow("1", i)

cv2.waitKey(0)