import numpy as np
import cv2

# **********************************
# COLORS
# **********************************
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# initializing canvas as a 300x300 canvas, with 3 channels (R, G, B)
# "zeros" indicate that values will be set to black, initially
canvas = np.zeros((300, 300, 3), dtype="uint8")

# **********************************
# LINES
# **********************************

# draw a green line from top-left to bottom-right
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)


# draw a red line from bottom-left to top-right, three pixels thick
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# **********************************
# RECTANGLES
# **********************************

# draw a green 50x50 square, starting at (10, 10) and ending at (60, 60)
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# draw a red rectangle, 5 pixels thick
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# draw another rectangle, blue and filled in ("-1")
cv2.rectangle(canvas, (200, 50), (255, 125), blue, -1)
cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# **********************************
# CIRCLES
# **********************************
canvas = np.zeros((300, 300, 3), dtype="uint8")

(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
#cv2.waitKey(0)

for i in range(0, 25):
    # randomly generate a radius size between 5 and 200;
    # generate a random color and then pick a random point
    # on our canvas where the circle will be drawn
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size = (3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))

    # draw random circle
    # "-1" at the end of arguments indicates solid color rather than line
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# **********************************
# DRAWING ON EXISTING IMAGE
# **********************************

image = cv2.imread("../florida_trip.png")

# we're going to draw an image around the face in the picture
cv2.circle(image, (168, 188), 90, (0, 0, 255), 2)
cv2.circle(image, (150, 164), 10, (0, 0, 255), -1)
cv2.circle(image, (192, 174), 10, (0, 0, 255), -1)
cv2.rectangle(image, (134, 200), (186,218), (0, 0, 255), -1)

cv2.imshow("Output", image)
cv2.waitKey(0)