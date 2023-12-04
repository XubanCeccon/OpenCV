
import cv2
import math
import numpy as np
 

def mse(img1, img2):
   # Assuming both images have the same shape
   h, w, color_channels = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse



def PSNR(img1, img2): 
    mse1 = mse(img1,img2)
    if(mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse1)) 
    return psnr 


img = cv2.imread('../images/road.jpg')
h, w, channels = img.shape
half = w//2
 
left_part = img[:, :half] 
right_part = img[:, half:]


cv2.imwrite("../images/compressed_lossy.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 10])
image_compressed = cv2.imread('../images/compressed_lossy.jpg')

cv2.imwrite("../images/image_left_compressed.jpg", left_part, [cv2.IMWRITE_JPEG_QUALITY, 10])
image_compressed_left = cv2.imread('../images/image_left_compressed.jpg')


cv2.imwrite("../images/image_right_compressed.jpg", right_part, [cv2.IMWRITE_JPEG_QUALITY, 10])
image_compressed_right = cv2.imread('../images/image_right_compressed.jpg')






MSE_left = mse(image_compressed_left, left_part)
MSE_right = mse(image_compressed_right, right_part)
MSE_original = mse(img,image_compressed)
print(MSE_original)
print(MSE_left)
print(MSE_right)
print((MSE_left+MSE_right)/2)







cv2.imshow('Left part', left_part)
cv2.imshow('Right part', right_part)

cv2.waitKey(0)  
cv2.destroyAllWindows()  