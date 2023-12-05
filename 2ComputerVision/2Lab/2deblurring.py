import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/road.jpg')
img = cv2.imread('../images/road.jpg', cv2.IMREAD_GRAYSCALE)

gaussian = cv2.GaussianBlur(img, (7, 7), 5,5)
side_by_side_gaussian = np.hstack((img, gaussian))
cv2.imshow('Gaussian', side_by_side_gaussian)
cv2.waitKey(0)




dft_gaussian = cv2.dft(np.float32(gaussian),flags = cv2.DFT_COMPLEX_OUTPUT)

dft_original = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)

dft_PSD = dft_gaussian/(dft_original)

dft_restored = dft_gaussian/(dft_PSD+0.0001)
restored_image = cv2.idft(dft_restored,flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
restored_image = cv2.normalize(restored_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)


dft = dft_restored
print(restored_image)


cv2.imshow('Restored', restored_image)
cv2.waitKey(0)






dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

""" plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
 """



cv2.destroyAllWindows()
