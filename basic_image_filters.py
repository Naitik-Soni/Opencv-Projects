import cv2

# Load the image
image_path = r"P:\Computer vision Experiments\Sample images\image6.jpg"
image = cv2.imread(image_path)

# Resizing the image for fitting into the window
h, w = image.shape[:2]
resize_fac = 0.7
image = cv2.resize(image, (int(w*resize_fac), int(h*resize_fac)))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# -----------------------------------------------------------------------
# All other operations goes here

avging = cv2.blur(image,(10,10))
cv2.imshow('Averaging',avging)

# Gaussian Blurring
# Again, you can change the kernel size
gausBlur = cv2.GaussianBlur(image, (5,5),0) 
cv2.imshow('Gaussian Blurring', gausBlur)

# Median blurring
medBlur = cv2.medianBlur(image,5)
cv2.imshow('Media Blurring', medBlur)

# Bilateral Filtering
bilFilter = cv2.bilateralFilter(image,21,75,75)
cv2.imshow('Bilateral Filtering', bilFilter)

# ----------------------------------------------------------------------

# Display the images
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()