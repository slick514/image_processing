# import the necessary packages
import cv2

image = cv2.imread("../../images/pyimagesearch_logo.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# apply a series of erosions
for i in range(0, 3):
	eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
	cv2.imshow("Eroded {} times".format(i + 1), eroded)

cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# apply a series of dilations
for i in range(0, 3):
	dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
	cv2.imshow("Dilated {} times".format(i + 1), dilated)

cv2.waitKey(0)