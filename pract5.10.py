import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("hollyhock.jpg", 0)

scratched = img.copy()
cv2.line(scratched, (30, 100), (220, 120), 0, 3)
cv2.line(scratched, (100, 30), (120, 220), 0, 3)
cv2.imwrite("scratched.png", scratched)

plt.imshow(scratched, cmap="gray")
plt.title("Scratched Image")
plt.axis("off")
plt.show()
