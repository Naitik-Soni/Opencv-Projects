import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image_path = r"P:\Computer vision Experiments\Sample images\bed.jpg"
image = cv2.imread(image_path)

# Resizing the image for fitting into the window
h, w = image.shape[:2]
resize_fac = 0.3
image = cv2.resize(image, (int(w*resize_fac), int(h*resize_fac)))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ----------------------------------------------------------------------

canny1 = cv2.Canny(image, 0, 64)
cv2.imshow("Canny 1", canny1)

canny2 = cv2.Canny(image, 64, 128)
cv2.imshow("Canny 2", canny2)

canny3 = cv2.Canny(image, 128, 192)
cv2.imshow("Canny 3", canny3)

canny4 = cv2.Canny(image, 192, 255)
cv2.imshow("Canny 4", canny4)

# ----------------------------------------------------------------------

# Display the images
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()