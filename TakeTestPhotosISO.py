from picamera import PiCamera
from time import sleep
import os

#https://www.raspberrypi.org/documentation/raspbian/applications/camera.md


root_folder = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")

folder = os.listdir(root_folder + "/TestImages")
num_folder_items = len(folder)
print(os.mkdir((root_folder + "/TestImages/Run%s") % str(num_folder_items + 1)))
camera = PiCamera(resolution=(1920,1080))
camera.start_preview()
sleep(5)

for i in range(0,9):
    camera.iso=(i*100)
    sleep(5)
    camera.capture((root_folder + "/TestImages/Run%s/Original_Photo_%s.jpg") %(num_folder_items + 1,i*100))
