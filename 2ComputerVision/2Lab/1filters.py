import cv2
import numpy as np

img = cv2.imread('../images/road.jpg')
Gaussian = cv2.GaussianBlur(img, (7, 7), 5,5) 


side_by_side = np.hstack((img, Gaussian)) 
cv2.imshow('Loaded image', side_by_side)


cv2.waitKey(0)  
cv2.destroyAllWindows()  