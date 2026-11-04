import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("hollyhock.jpg", 0)

s_p_img = img.copy()
num_noise = 2000

coords = [np.random.randint(0, i-1, num_noise) for i in img.shape]
s_p_img[tuple(coords)] = 255

coords = [np.random.randint(0, i-1, num_noise) for i in img.shape]
s_p_img[tuple(coords)] = 0

cv2.imwrite("noisy_salt_pepper.png", s_p_img)
plt.imshow(s_p_img, cmap="gray")
plt.title("Salt & Pepper Noise")
plt.axis("off")
plt.show()
