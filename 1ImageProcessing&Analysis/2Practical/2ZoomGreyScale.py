import cv2
import numpy as np

# Mouse callback function
def colour_query_mouse_callback(event, x, y, flags, img_greyscale):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Left button prints color information at click location
        cropped_image = img_greyscale[(y-50):(y+50), (x-50):(x+50)]
        cv2.destroyWindow("cropppedddd")

        print(f"Colour information at image location ({x},{y}): ", end="")
        for channel in range(1):  # Three channels (B, G, R)
            print(int(img_greyscale[y, x]), end=" ")

        cv2.imshow("cropppedddd",cropped_image)

        print()
        

    elif event == cv2.EVENT_RBUTTONDOWN:
        # Right button sets color information at click location to white
        print(f"Colour information at image location ({x},{y}) set to white.", end=" ")
       
        for i in range (-2,3):
            for j in range (-2,3):
                 img_greyscale[y+i, x+j] = 255
        print()

    

# Main function
def main(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    img_greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if img_greyscale is None:
        print("Error: Image could not be read.")
        return -1

    window_name = "OPENCV: colour query"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, colour_query_mouse_callback, img_greyscale)
    print(f"Image: (width x height) = ({img_greyscale.shape[1]} x {img_greyscale.shape[0]})")
    print(f"Colour channels = {img_greyscale.shape[1]}")

    keep_processing = True
    while keep_processing:
        cv2.imshow(window_name, img_greyscale)
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
