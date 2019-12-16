from dotenv import load_dotenv
import os
import SMSHandler as SMSHandler
import EmailHandler as EmailHandler
import ImageHandler as ImageHandler
import time

load_dotenv()

twilio_account_sid = os.getenv("account_sid")
twilio_auth_token = os.getenv("auth_token")
email_list = os.getenv("email_list")
gmail_pass = os.getenv("gmail_pass")

test_imgs = ['/OneplusPhotos/10.jpg','/OneplusPhotos/2.jpg', '/OneplusPhotos/5.jpg', '/OneplusPhotos/6.jpg']

while True:
    
    doors_open = ImageHandler.check_garage_doors_open(test_imgs[3])
    time.sleep(300)
    
    if doors_open != None:

        doors_open2 = ImageHandler.check_garage_doors_open(test_imgs[3])

        if doors_open == doors_open2:
            EmailHandler.send_email(email_list=email_list, gmail_pass=gmail_pass, door_open=doors_open2)
            #SMSHandler.send_sms(door_open=doors_open2, account_sid=twilio_account_sid, auth_token=twilio_auth_token)