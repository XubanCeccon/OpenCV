import cv2

image = cv2.imread('../Images/zyzz.jpg')
image = cv2.imread('../Images/Donosti.png')

if image is None:
    print("Could not open or find the image")
else:

    Gaussian = cv2.GaussianBlur(image, (111, 111), 100, 10) 
    grayscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    flippled_image = cv2.flip(image, 0) 
    canny_image = cv2.Canny(image,300,400)
    #resized_image = cv2.resize(image,(100,200),interpolation=cv2.INTER_NEAREST)
    resized_image = cv2.resize(image,(100,200),interpolation=cv2.INTER_LINEAR)


    cv2.imshow('Original Image', image)
    cv2.imshow('Gaussian Image', Gaussian)
    cv2.imshow('Grayscale image', grayscale_img)
    cv2.imshow('flipped image', flippled_image)
    cv2.imshow('Canny image', canny_image)
    cv2.imshow('Resized image', resized_image)




    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

