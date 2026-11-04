import cv2
import numpy
img = cv2.imread("Hollyhock.jpg")
dst = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
cv2.imshow('image', numpy.hstack((img, dst)))
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)