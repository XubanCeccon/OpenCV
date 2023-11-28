import cv2

def main():
    window_name = "OpenCV: Live Image Display"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera")
        exit(0)

    ret, img = cap.read()

    if not ret:
        print("Error: Could not grab a frame")
        exit(0)

    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
