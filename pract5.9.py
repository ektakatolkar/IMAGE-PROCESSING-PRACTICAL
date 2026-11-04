import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("hollyhock.jpg", 0)

noise = np.random.randint(0, 50, img.shape, dtype=np.uint8)
noisy_img = cv2.add(img, noise)
cv2.imwrite("noisy_image.png", noisy_img)

plt.imshow(noisy_img, cmap="gray")
plt.title("General Noisy Image")
plt.axis("off")
plt.show()
