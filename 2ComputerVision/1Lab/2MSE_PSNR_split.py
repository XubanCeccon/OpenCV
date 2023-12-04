
import cv2
 
img = cv2.imread('../images/road.jpg')
h, w, channels = img.shape
half = w//2
 
left_part = img[:, :half] 
right_part = img[:, half:] 










cv2.imshow('Left part', left_part)
cv2.imshow('Right part', right_part)

cv2.waitKey(0)  
cv2.destroyAllWindows()  