import cv2
import numpy as np

capture = cv2.VideoCapture(r"P:\Computer vision Experiments\Sample images\video.mp4")

# =============================================================
def processimg(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([0, 0, 0])   # lower bound H, S, V
    upper_blue = np.array([180, 255, 60])  # upper bound H, S, V

    # Create mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # h,s,v = cv2.split(hsv)
    # Apply mask to the original image (optional)
    return cv2.bitwise_and(img, img, mask=mask)
    # return h,s,v

def colorInv(img):
    return cv2.split(img)

# cv2.imshow("Masked", result)

# =============================================================
while True:
    ret, frame = capture.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    rf = 0.2

    img = cv2.resize(frame, (int(w * rf), int(h * rf)))
    img = img[int(h*0.25*0.2): int(h*0.75*0.2), :]
    b,g,r = colorInv(img)

    zero = np.zeros_like(b)
    cv2.imshow("OG", img)
    cv2.imshow("Only Blue", cv2.merge([b, zero, zero]))
    cv2.imshow("Only Green", cv2.merge([zero, g, zero]))
    cv2.imshow("Only Red", cv2.merge([zero, zero, r]))
    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()