import cv2
import numpy as np
import os

script_path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
print(script_path)
test_imgs = ['/OneplusPhotos/2.jpg', '/OneplusPhotos/5.jpg', '/OneplusPhotos/6.jpg', '/OneplusPhotos/10.jpg', '/OneplusPhotos/11.jpg', '/OneplusPhotos/12.jpg', '/OneplusPhotos/13.jpg']
#test_imgs = ['/OneplusPhotos/5.jpg']




for imgName in test_imgs:
    img = cv2.imread(script_path + imgName)
    cv2.imwrite(script_path + "/Output Photos/Original_Photo.jpg", img)
    height, width, channels = img.shape

    # light_red = np.array([91, 8, 157], dtype="uint8")
    # dark_red = np.array([111, 28, 237], dtype="uint8")

    #this detects light
    # light_red2 = np.array([0, 0, 130], dtype="uint8")
    # dark_red2 = np.array([180, 150, 255], dtype="uint8")

    # this detects brown

    light_red1 = np.array([0, 25, 20], dtype="uint8")
    dark_red1 = np.array([20, 255, 255], dtype="uint8")
    light_red2 = np.array([170, 25, 20], dtype="uint8")
    dark_red2 = np.array([180, 255, 255], dtype="uint8")
    # light_red2 = light_red1
    # dark_red2 = dark_red1


    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv_img, light_red1, dark_red1)
    mask2 = cv2.inRange(hsv_img, light_red2, dark_red2)

    mask = mask1 | mask2

    cropped_img_left = mask[753:1134, 975:2136]
    cropped_img_right = mask[967:1186, 2643:3729]

    
    # cropped_img_right = mask[y:y+h, x:x+w]

    left_pixel_threshold = 100000
    right_pixel_threshold = 150000

    if (cv2.countNonZero(cropped_img_left) < left_pixel_threshold):
        left_open = True
    else:
        left_open = False

    print(cv2.countNonZero(cropped_img_right))

    if (cv2.countNonZero(cropped_img_right) < right_pixel_threshold):
        right_open = True
    else:
        right_open = False


    print ("left_open: " + str(left_open) + " right open: " + str(right_open))

    cv2.rectangle(hsv_img, (975,753), (2136,1134), (255, 0, 0) , 5)
    cv2.rectangle(hsv_img, (2643,967), (3729,1186), (255, 0, 0) , 5)


    cv2.namedWindow("imagewindow", cv2.WINDOW_NORMAL)
    cv2.imshow('imagewindow', hsv_img)
    cv2.namedWindow("croppedimg", cv2.WINDOW_NORMAL)
    cv2.imshow('croppedimg', cropped_img_right)
    cv2.namedWindow("maskedwindow", cv2.WINDOW_NORMAL)
    cv2.imshow('maskedwindow', mask)
    key = cv2.waitKey(0)

    if key == 49:
        exit()