import cv2
import sys

img_original = cv2.imread("../Images/Donosti.png")
img_original_grayscale = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)


img_twice_inverted = cv2.imread("twiceInverted.jpg")
img_twice_inverted_grayscale = cv2.cvtColor(img_twice_inverted, cv2.COLOR_BGR2GRAY)

diff = img_original.copy()




cv2.equalizeHist(img_twice_inverted,img_twice_inverted_grayscale,diff)
cv2.imshow('Difference image', diff)



cv2.waitKey(0)
cv2.destroyAllWindows()