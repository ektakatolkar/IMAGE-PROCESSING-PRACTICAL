import cv2
import numpy as np
img = cv2.imread('Hollyhock.jpg')
if img is None:
    print("Error: Image not found or path is incorrect.")
    exit()
dst = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('Original vs Bilateral Filter', np.hstack((img, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()
