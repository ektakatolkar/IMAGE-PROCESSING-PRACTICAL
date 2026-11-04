import numpy as np
import cv2 as cv
img = cv.imread('Hollyhock.jpg', 0)
cropped_img = img[100:300, 100:300]
cv.imshow('Cropped Image', cropped_img)
cv.imwrite('cropped_out.jpg', cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()
