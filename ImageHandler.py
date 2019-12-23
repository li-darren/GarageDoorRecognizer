WINDOWS_DEV = False
RASPBERRYPI_TEST = True
import cv2 as cv2
import numpy as np
if not WINDOWS_DEV:
    from picamera import PiCamera
from time import sleep

def check_garage_doors_open (root_folder):

    if not WINDOWS_DEV:
        camera = PiCamera(resolution=(1920,1080))
        camera.start_preview()
        sleep(5)
        camera.capture(root_folder + "/OutputPhotos/Original_Photo.jpg")
        camera.stop_preview()
        camera.close()

    img = cv2.imread(root_folder + "/OutputPhotos/Original_Photo.jpg")

    left_pixel_threshold = 100000
    right_pixel_threshold = 150000
    
    light_red1 = np.array([0, 5, 5], dtype="uint8")
    dark_red1 = np.array([70, 255, 255], dtype="uint8")
    light_red2 = np.array([160, 5, 5], dtype="uint8")
    dark_red2 = np.array([180, 255, 255], dtype="uint8")


    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.rectangle(hsv_img, (238,273), (831,516), (255, 0, 0) , 5)
    cv2.rectangle(hsv_img, (1065,276), (1564,445), (255, 0, 0) , 5)

    cv2.imwrite(root_folder + "/OutputPhotos/HSV_Photo.jpg", hsv_img)

    mask1 = cv2.inRange(hsv_img, light_red1, dark_red1)
    mask2 = cv2.inRange(hsv_img, light_red2, dark_red2)

    mask = mask1 | mask2

    cv2.imwrite(root_folder + "/OutputPhotos/Mask_Photo.jpg", mask)

    cropped_img_left = mask[273:516, 238:831]
    cropped_img_right = mask[276:445, 1065:1564]

    print("left nonzero: " + str(cv2.countNonZero(cropped_img_left)))
    print("right nonzero: " + str(cv2.countNonZero(cropped_img_right)))


    if (cv2.countNonZero(cropped_img_left) < left_pixel_threshold):
        left_open = True
    else:
        left_open = False

    if (cv2.countNonZero(cropped_img_right) < right_pixel_threshold):
        right_open = True
    else:
        right_open = False


    print ("left_open: " + str(left_open) + " right open: " + str(right_open))

    if WINDOWS_DEV:
        cv2.namedWindow("imagewindow", cv2.WINDOW_NORMAL)
        cv2.imshow('imagewindow', img)
        cv2.namedWindow("hsvimagewindow", cv2.WINDOW_NORMAL)
        cv2.imshow('hsvimagewindow', hsv_img)
        cv2.namedWindow("croppedimgleft", cv2.WINDOW_NORMAL)
        cv2.imshow('croppedimgleft', cropped_img_left)
        cv2.namedWindow("croppedimgright", cv2.WINDOW_NORMAL)
        cv2.imshow('croppedimgright', cropped_img_right)
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

if WINDOWS_DEV:
    check_garage_doors_open("F:\Windows 10 User Files\Windows 10 User Files - Darren\OneDrive - University of Waterloo\_Side Projects\GarageDoorRecognizer")
if RASPBERRYPI_TEST:
    check_garage_doors_open("/home/pi/Desktop/GarageDoorRecognizer")
