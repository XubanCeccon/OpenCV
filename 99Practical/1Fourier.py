# import required libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt

# read input image
img = cv2.imread('../Images/Donosti.png',0)
img = cv2.imread('../Images/CranfieldAirport.jpeg',0)
img = cv2.imread('../Images/images.png',0)
img = cv2.imread('../Images/chessboard.png',0)



# find the discrete fourier transform of the image
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)

# shift zero-frequency component to the center of the spectrum
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv2.magnitude(
      dft_shift[:,:,0],
      dft_shift[:,:,1])
   )
# visualize input image and the magnitude spectrum
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'coolwarm')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()