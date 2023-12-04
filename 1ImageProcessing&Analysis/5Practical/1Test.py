import cv2
import sys

def capture_video(output_file, n_frames=100):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not grab a frame")
        sys.exit(0)

    ret, frame = cap.read()
    frame = cv2.GaussianBlur(frame, (3, 3), 2, 2)
    frame = cv2.Canny(frame,300,400)

    if not ret:
        print("Error: Could not grab a frame")
        sys.exit(0)

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter(output_file, fourcc, 25.0, (frame.shape[1], frame.shape[0]))

    if not out.isOpened():
        print("Error: Could not open video file")
        sys.exit(0)

    print("\nStarting video capture...")

    for i in range(n_frames):
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    print("Finished")

    cap.release()
    out.release()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <output_video>")
        sys.exit(-1)

    capture_video(sys.argv[1])
