import cv2
import numpy as np
img = cv2.imread("Hollyhock.jpg")
if img is None:
    print("Error: Image not found or path is incorrect.")
    exit()
im1 = cv2.blur(img, (5, 5))
im2 = cv2.boxFilter(img, -1, (2, 2), normalize=True)
cv2.imshow('Blurred (5x5) vs Box Filter (2x2)', np.hstack((im1, im2)))
cv2.waitKey(0)
cv2.destroyAllWindows()
