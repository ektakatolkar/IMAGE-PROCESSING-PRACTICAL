import cv2
img = cv2.imread('Hollyhock.jpg', 0)
negative = 255 - img
import numpy as np
combined = np.hstack((img, negative))
cv2.imshow('Original (Left) vs Negative (Right)', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()