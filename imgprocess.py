import cv2
import numpy
import os

script_path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
print(script_path)
test_imgs = ['/OneplusPhotos/2.jpg', '/OneplusPhotos/5.jpg', '/OneplusPhotos/6.jpg', '/OneplusPhotos/10.jpg', '/OneplusPhotos/11.jpg']
#test_imgs = ['/OneplusPhotos/5.jpg']




for imgName in test_imgs:
    img = cv2.imread(script_path + imgName)
    height, width, channels = img.shape

    mask = numpy.zeros((height+2, width+2), numpy.uint8)
    
    starting_pixel = (1472,912)


    diff = (2,2,2)

    alpha = 0.015 #contrast control
    beta = 0.06 #brightness control

    #colorchanged = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)

    #floodfilled_image = cv2.floodFill(new_img, mask, starting_pixel, (0, 255, 0), diff, diff)
    cv2.circle(img, starting_pixel, 10, (255,0,0), 5)



    # cv2.namedWindow("imagewindow", cv2.WINDOW_NORMAL)
    # cv2.imshow('imagewindow', new_img)
    cv2.waitKey(0)