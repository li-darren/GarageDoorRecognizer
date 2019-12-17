import cv2 as cv2
import numpy as np
from picamera import PiCamera
from time import sleep
def check_garage_doors_open (root_folder):

    
    #cv2.namedWindow("originalimg", cv2.WINDOW_NORMAL)

    camera = PiCamera()
    camera.start_preview()
    sleep(100)
    #camera.capture(root_folder + "/Output Photos/Original_Photo.jpg")
    
    left_pixel_threshold = 100000
    right_pixel_threshold = 150000
    
    light_red1 = np.array([0, 25, 20], dtype="uint8")
    dark_red1 = np.array([20, 255, 255], dtype="uint8")
    light_red2 = np.array([170, 25, 20], dtype="uint8")
    dark_red2 = np.array([180, 255, 255], dtype="uint8")


    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv_img, light_red1, dark_red1)
    mask2 = cv2.inRange(hsv_img, light_red2, dark_red2)

    mask = mask1 | mask2

    cropped_img_left = mask[753:1134, 975:2136]
    cropped_img_right = mask[967:1186, 2643:3729]

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
    cv2.waitKey(0)

    if right_open and left_open:
        return "both"
    elif right_open:
        return "right"
    elif left_open:
        return "left"
    else:
        return None