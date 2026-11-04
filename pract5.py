import cv2
import numpy as np
damaged_img = cv2.imread("cat.png")
height, width = damaged_img.shape[0], damaged_img.shape[1]
mask_gray = np.where(np.all(damaged_img == 0, axis=-1), 255, 0).astype(np.uint8)
cv2.imwrite("mask.png", mask_gray)
restored_telea = cv2.inpaint(damaged_img, mask_gray, 3, cv2.INPAINT_TELEA)
restored_ns = cv2.inpaint(damaged_img, mask_gray, 3, cv2.INPAINT_NS)
cv2.imwrite("restored_telea.png", restored_telea)
cv2.imwrite("restored_ns.png", restored_ns)
cv2.imshow("Original Damaged Image", damaged_img)
cv2.imshow("Generated Mask", mask_gray)
cv2.imshow("Restored (Telea)", restored_telea)
cv2.imshow("Restored (Navier-Stokes)", restored_ns)
cv2.waitKey(0)
cv2.destroyAllWindows()
