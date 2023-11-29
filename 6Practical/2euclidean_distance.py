import cv2
import numpy as np
import math

coordinates = [0,0,0,0]
counter = [0]


def colour_query_mouse_callback(event, x, y, flags, img):

    if event == cv2.EVENT_LBUTTONDOWN:        
        if counter[0] == 0:
            coordinates[0] = x
            coordinates[1] = y
            print(f"fist click! in ({x},{y} ")
            counter[0] = 1

        else:
            coordinates[2] = x
            coordinates[3] = y
            euclidean_distance = math.sqrt((coordinates[0]-coordinates[2])**2 +(coordinates[1]-coordinates[3])**2)
            print(f"Second click in ({x},{y}), the  Euclidean distance is:({euclidean_distance}): ", end="")
            counter[0] = 0
            

    
# Main function
def main(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    img_greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if img is None:
        print("Error: Image could not be read.")
        return -1

    window_name = "OPENCV: colour query"
    cv2.namedWindow(window_name)
    firstclick = True

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
