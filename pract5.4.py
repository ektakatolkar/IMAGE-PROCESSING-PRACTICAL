import cv2
import matplotlib.pyplot as plt
img = cv2.imread("Hollyhock.jpg", 0)
restored = cv2.medianBlur(img, 5)
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Salt & Pepper Noise")
plt.subplot(1, 2, 2)
plt.imshow(restored, cmap='gray')
plt.title("Restored (Median Filter)")
plt.show()
