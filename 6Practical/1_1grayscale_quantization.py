import cv2
image = cv2.imread('../Images/Conquer.jpeg')

grayscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("Conquer_grayscale.jpeg", grayscale_img, [cv2.IMWRITE_JPEG_QUALITY, 100])
