import cv2
import numpy as np

# Load the image
image_path = r"P:\Computer vision Experiments\Sample images\new_lena.png"
image = cv2.imread(image_path)

# Resizing the image for fitting into the window
h, w = image.shape[:2]
resize_fac = 1
image = cv2.resize(image, (int(w*resize_fac), int(h*resize_fac)))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ----------------------------------------------------------------------

# (1) Kernel based sharpening
kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
sharpened = cv2.filter2D(image, -1, kernel)
cv2.imshow('kernel based', sharpened)

# (2) Unsharp masking
blurred = cv2.GaussianBlur(image, (9, 9), 10)
sharpened = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)
cv2.imshow('unsharp masking 1', sharpened)

# (3) Laplacian sharpening
laplacian = cv2.Laplacian(image, cv2.CV_64F)
sharpened = cv2.convertScaleAbs(image - 0.7 * laplacian)
cv2.imshow('Laplacian', sharpened)

# (4) High boost filtering
A = 2.5
blurred = cv2.GaussianBlur(image, (5, 5), 0)
mask = cv2.subtract(image, blurred)
high_boost = cv2.addWeighted(image, A, blurred, -(A-1), 0)
cv2.imshow('Highboost filtering', high_boost)

# (5) Sobel
# sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
# sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
# sobel = cv2.magnitude(sobelx, sobely)
# sobel = cv2.convertScaleAbs(sobel)
# cv2.imshow('Sobel', sobel)

# (6) CLAHE Sharpening
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# enhanced = clahe.apply(gray)
# laplacian = cv2.Laplacian(enhanced, cv2.CV_64F)
# sharpened = cv2.convertScaleAbs(enhanced - 0.5 * laplacian)
# cv2.imshow('CLAHE', sharpened)

# ----------------------------------------------------------------------

# Display the images
cv2.imshow("Original", image)
# cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
