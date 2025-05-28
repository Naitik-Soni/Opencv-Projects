import cv2
import numpy as np

# Load the image
image_path = r"P:\Computer vision Experiments\Sample images\image4.jpg"
image = cv2.imread(image_path)

# Resizing the image for fitting into the window
h, w = image.shape[:2]
resize_fac = 0.5
image = cv2.resize(image, (int(w*resize_fac), int(h*resize_fac)))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# -----------------------------------------------------------------------
# All other operations goes here



# ----------------------------------------------------------------------

# Display the images
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()