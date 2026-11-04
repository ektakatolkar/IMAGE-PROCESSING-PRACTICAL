import cv2
import numpy as np
img = cv2.imread("Hollyhock.jpg")
if img is None:
    print("Error: Image not found or path is incorrect.")
    exit()
ksize = 5
im1 = cv2.medianBlur(img, ksize)
cv2.imshow('Original vs Median Blur', np.hstack((img, im1)))
cv2.waitKey(0)
cv2.destroyAllWindows()
