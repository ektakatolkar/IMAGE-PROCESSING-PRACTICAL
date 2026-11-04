import cv2
import matplotlib.pyplot as plt
img = cv2.imread("Hollyhock.jpg", 0)
restored = cv2.GaussianBlur(img, (5, 5), 0)
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title("Gaussian Noisy")
plt.subplot(1, 2, 2), plt.imshow(restored, cmap='gray'), plt.title("Restored (Gaussian Blur)")
plt.show()