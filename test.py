import cv2

# Load an image
image = cv2.imread('zyzz.jpg')  # Replace with your image path

# Check if the image was successfully loaded
if image is None:
    print("Could not open or find the image")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original image
    cv2.imshow('Original Image', image)

    # Display the grayscale image
    cv2.imshow('Grayscale Image', gray_image)

    # Wait for a key press and then close all open windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

