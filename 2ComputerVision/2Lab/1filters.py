import cv2
import numpy as np

img = cv2.imread('../images/road.jpg')

gaussian = cv2.GaussianBlur(img, (7, 7), 5,5)
side_by_side_gaussian = np.hstack((img, gaussian))
cv2.imshow('Gaussian', side_by_side_gaussian)
cv2.waitKey(0)

median = cv2.medianBlur(img,5)
side_by_side_median = np.hstack((img, median))
cv2.imshow('Median', side_by_side_median)
cv2.waitKey(0)

#This blur preserves the edges!
bilateral = cv2.bilateralFilter(img,9,75,75)
side_by_side_bilateral = np.hstack((img, bilateral))
cv2.imshow('Bilateral', side_by_side_bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()