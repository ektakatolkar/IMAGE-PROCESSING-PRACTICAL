import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('Hollyhock.jpg')
filtered_image_bgr = cv2.medianBlur(image, 11)
cv2.imwrite('Median Blur.jpg', filtered_image_bgr)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
filtered_image_rgb = cv2.cvtColor(filtered_image_bgr, cv2.COLOR_BGR2RGB)
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image_rgb)
plt.subplot(1, 2, 2)
plt.title("Median Blur")
plt.imshow(filtered_image_rgb)
plt.show()
