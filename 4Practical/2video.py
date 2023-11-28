import cv2
def main():
    counter = 0
    counter2 = 0

    window_name = "OpenCV: Live Video Display"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera")
        exit(0)

    n_frames = 500
    for i in range(n_frames):
        ret, img = cap.read()

        if not ret:
            print("Error: Could not grab a frame")
            break
        
        #diff2 = img_original.copy()



        #cv2.absdiff(img_original,img_inverted,diff1)

        output_img = cv2.GaussianBlur(img, (111, 11), 10, 0)
        cv2.circle(output_img,(447,63), 63, (0,0,255), -1)

       # output_img =

        cv2.imshow(window_name, output_img)
        cv2.waitKey(33)
        #print(cv2.getTickCount())
        print(counter)
        counter = counter +1
        counter2 = counter2 + 1
        if (counter >= 30):
            counter = 0
            cv2.imwrite("output.jpg", output_img, [cv2.IMWRITE_JPEG_QUALITY, 5])
        if (counter2>=200):
            cv2.imwrite("output2.jpg", output_img, [cv2.IMWRITE_JPEG_QUALITY, 5])

        key = cv2.waitKey(10)

        if key == ord('s'): 
            cv2.imwrite("snapshot.jpg", output_img, [cv2.IMWRITE_JPEG_QUALITY, 5])



    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
