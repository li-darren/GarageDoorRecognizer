from picamera import PiCamera
from time import sleep
import os

#https://www.raspberrypi.org/documentation/raspbian/applications/camera.md


root_folder = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")

num_folders = os.listdir(root_folder + "/TestImages")
number_files = len(num_folders)

camera = PiCamera()
camera.start_preview()
sleep(5)

for i in range(0,8):
    camera.iso=(i*100)
    camera.capture((root_folder + "/TestImages/Run%s/Original_Photo_%s.jpg") %(len(num_folders) + 1,i*100))
    sleep(5)
