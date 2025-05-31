import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image_path = r"P:\Computer vision Experiments\Sample images\cube.jpg"
image = cv2.imread(image_path)

# Resizing the image for fitting into the window
h, w = image.shape[:2]
resize_fac = 0.7
image = cv2.resize(image, (int(w*resize_fac), int(h*resize_fac)))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ----------------------------------------------------------------------

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)

cv2.imshow("Sobel", sobel)

# ----------------------------------------------------------------------

# Display the images
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()