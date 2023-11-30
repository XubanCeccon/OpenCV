import cv2
import numpy as np

def apply_vapor_trails(frames, weights):
    vapor_trail = np.zeros_like(frames[0], dtype=float)
    for i, frame in enumerate(frames):
        vapor_trail += weights[i] * frame
    vapor_trail = cv2.normalize(vapor_trail, None, 0, 255, cv2.NORM_MINMAX)
    return np.uint8(vapor_trail)

def apply_low_pass_filter(image):
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols), np.uint8)
    mask[crow-30:crow+30, ccol-30:ccol+30] = 1
    fshift = fshift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    return np.abs(img_back)

def color_slicing(image, hsv_low, hsv_high):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, hsv_low, hsv_high)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result

# Initialize webcam
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
vapor_frames = [prev_frame] * 5  # Number of frames for vapor trails
vapor_weights = [1/5] * 5  # Equal weights for vapor trails

while True:
    ret, frame = cap.read()

    # Task 1: Difference Image
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff_image = cv2.absdiff(prev_frame, gray_frame)
    cv2.imshow('Difference Image', diff_image)
    prev_frame = gray_frame

    # Task 2: Vapor Trails
    vapor_frames.pop(0)
    vapor_frames.append(gray_frame)
    vapor_image = apply_vapor_trails(vapor_frames, vapor_weights)
    cv2.imshow('Vapor Trails', vapor_image)

    # Task 3 and 4: Grayscale Histogram and Adaptive Thresholding
    adaptive_thresh = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imshow('Adaptive Threshold', adaptive_thresh)

    # Task 5: Low-Pass Filtering in Fourier Space
    low_pass_image = apply_low_pass_filter(gray_frame)
    cv2.imshow('Low Pass Filtered Image', low_pass_image)

    # Task 6: Real-time Colour-slicing
    # Define the HSV range for the color you want to slice
    hsv_lower = np.array([110,50,50])
    hsv_upper = np.array([130,255,255])
    color_sliced_image = color_slicing(frame, hsv_lower, hsv_upper)
    cv2.imshow('Color Slicing', color_sliced_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
