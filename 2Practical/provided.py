import cv2
import numpy as np

# Mouse callback function
def colour_query_mouse_callback(event, x, y, flags, img):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Left button prints color information at click location
        print(f"Colour information at image location ({x},{y}): ", end="")
        for channel in range(3):  # Three channels (B, G, R)
            print(int(img[y, x, channel]), end=" ")
        print()

    elif event == cv2.EVENT_RBUTTONDOWN:
        # Right button sets color information at click location to white
        print(f"Colour information at image location ({x},{y}) set to white.", end=" ")
        img[y, x] = [255, 255, 255]  # Set the pixel to white
        print()

# Main function
def main(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if img is None:
        print("Error: Image could not be read.")
        return -1

    window_name = "OPENCV: colour query"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, colour_query_mouse_callback, img)

    print(f"Image: (width x height) = ({img.shape[1]} x {img.shape[0]})")
    print(f"Colour channels = {img.shape[2]}")

    keep_processing = True
    while keep_processing:
        cv2.imshow(window_name, img)
        key = cv2.waitKey(20)

        if key == ord('x'):
            print("Keyboard exit requested, exiting now - bye!")
            keep_processing = False

    return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        exit_code = main(sys.argv[1])
    else:
        print("Usage: python script.py <image_name>")
        exit_code = -1

    sys.exit(exit_code)
