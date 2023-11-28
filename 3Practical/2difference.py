import cv2
import sys
import numpy as np

img_original = cv2.imread("../Images/Donosti.png")
img_inverted = cv2.imread("inverted.jpg")
img_twice_inverted = cv2.imread("twiceInverted.jpg")
diff1 = img_original.copy()
diff2 = img_original.copy()



cv2.absdiff(img_original,img_inverted,diff1)
#cv2.imshow('Difference image', diff1)

cv2.absdiff(img_original,img_twice_inverted,diff2)
#cv2.imshow('Difference image between the original and double inverted one!!!!', diff2)


res = np.hstack((diff1, diff2)) 
  
# show image input vs output 
cv2.imshow("test", res) 


cv2.waitKey(0)
cv2.destroyAllWindows()