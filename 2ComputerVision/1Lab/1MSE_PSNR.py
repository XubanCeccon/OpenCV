import cv2
import numpy as np
import math
import os



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

list_of_images = ["cell.jpg", "chariot.jpg", "group.jpg", "road.jpg", "starrynight-2.jpg"]


    
 
values = []

for image_name in list_of_images:

    image_path = os.path.join('../images/', image_name)
    image_load = cv2.imread(image_path)
    cv2.imwrite("../images/image_compressed_lossy.jpg", image_load, [cv2.IMWRITE_JPEG_QUALITY, 10])
    image_compressed = cv2.imread('../images/image_compressed_lossy.jpg')


    
    error = mse(image_load, image_compressed)
    error2 = PSNR(image_load, image_compressed)
    values.append([error,error2])
    print("Loaded image: ",image_name," The error is : ", error ," and the PSNR is: " ,error2)
    side_by_side = np.hstack((image_load, image_compressed)) 
    cv2.imshow('image', side_by_side)

    cv2.waitKey(0)  
    cv2.destroyAllWindows()  
print(values)



