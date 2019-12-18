from picamera import PiCamera
from time import sleep
import os

#https://www.raspberrypi.org/documentation/raspbian/applications/camera.md


root_folder = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")

folder = os.listdir(root_folder + "/TestImages")
num_folder_items = len(folder)
os.mkdir((root_folder + "/TestImages/Run%s") % str(num_folder_items + 1))
camera = PiCamera()
camera.start_preview()
sleep(5)

exposure_modes = ['off','auto','night','nightpreview','backlight','spotlight','sports','snow','beach','verylong','fixedfps','antishake','fireworks']

for exposure_mode in exposure_modes:
    camera.exposure_mode=exposure_mode
    sleep(5)
    camera.capture((root_folder + "/TestImages/Run%s/Original_Photo_%s.jpg") %(num_folder_items + 1,exposure_mode))
