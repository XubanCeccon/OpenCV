import cv2
import math
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('../images/cell.jpg')
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 10]
h, w, channels = img.shape
step_x = w//8
step_y = h//8

def mse(img1, img2):
   # Assuming both images have the same shape
   h, w, color_channels = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse




data = []

for i in range (8):
    for j in range (8):
        tile = img[i * step_y:(i + 1) * step_y, j * step_x:(j + 1) * step_x]
        ret, tile_compressed = cv2.imencode('.jpg', tile, encode_param)
        tile_decompressed = cv2.imdecode(tile_compressed, cv2.IMREAD_COLOR)
        data.append(mse(tile,tile_decompressed))

        cv2.imshow('image', tile_decompressed)
        cv2.waitKey(0)  
        cv2.destroyAllWindows()
print(data)
mean_value = np.mean(data)
std_value = np.std(data)

print("Mean:", mean_value)
print("Standard Deviation:", std_value)

