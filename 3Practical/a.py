import cv2
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: prog <image_name> <output_img>")
        return -1

    input_image_name = sys.argv[1]
    output_image_name = sys.argv[2]

    input_img = cv2.imread(input_image_name, cv2.IMREAD_COLOR)

    if input_img is None:
        print("Image not found or unable to open")
        return -1

    output_img = cv2.bitwise_not(input_img)

    cv2.imwrite(output_image_name, output_img, [cv2.IMWRITE_JPEG_QUALITY, 80])
    cv2.imwrite(output_image_name, output_img, [cv2.CV_IMWRITE_PNG_COMPRESSION, 80])



    return 0

if __name__ == "__main__":
    sys.exit(main())
