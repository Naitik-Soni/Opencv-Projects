import cv2
import numpy as np

img_path = r"P:\Computer vision Experiments\Sample images\garden.jpg"

img = cv2.imread(img_path)
h, w = img.shape[:2]
rf = 0.4

img = cv2.resize(img, (int(w*rf), int(h*rf)))

# =============================================================

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([35, 150, 50])   # lower bound H, S, V
upper_blue = np.array([85, 255, 255])  # upper bound H, S, V

# Create mask
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Apply mask to the original image (optional)
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Masked", result)

# =============================================================

cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()