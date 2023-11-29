import cv2
image1 = cv2.imread('Conquer_grayscale.jpeg') # original
image2 = cv2.imread('Conquer_grayscale.jpeg') # 2
image3 = cv2.imread('Conquer_grayscale.jpeg') # 4
image4 = cv2.imread('Conquer_grayscale.jpeg') # 8
image5 = cv2.imread('Conquer_grayscale.jpeg') # 16
image6 = cv2.imread('Conquer_grayscale.jpeg') # 32
image7 = cv2.imread('Conquer_grayscale.jpeg') # 64
image8 = cv2.imread('Conquer_grayscale.jpeg') # 128
image9 = cv2.imread('Conquer_grayscale.jpeg') # 256



import numpy as np

# 8 * 32 = 256
step = 2

height = image1.shape[0]
print(height)
width = image1.shape[1]
print(width)

def myfunction(step,image):
    for i in range(500):
        for j in range(500):
            pixel = image[i,j]
            pixel // step
            pixel = pixel * step
            image[i,j] = pixel
    return image


image2 = myfunction(2,image1)
image3 = myfunction(4,image1)
image4 = myfunction(8,image1)
image5 = myfunction(16,image1)
image6 = myfunction(32,image1)
image7 = myfunction(64,image1)
image8 = myfunction(128,image1)
image9 = myfunction(256,image1)



multiple_images = np.hstack(( image1,image2,image3,image4, image5,image6,image7,image8,image9)) 


# show image input vs output 
cv2.imshow("test", multiple_images) 
cv2.imshow("test2", image5) 


cv2.waitKey(0)
cv2.destroyAllWindows()