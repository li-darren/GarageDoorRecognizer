from dotenv import load_dotenv
import os as os
import SMSHandler as SMSHandler
import EmailHandler as EmailHandler
import ImageHandler as ImageHandler
import time

load_dotenv()
root_folder = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
twilio_account_sid = os.getenv("account_sid")
twilio_auth_token = os.getenv("auth_token")
email_list = os.getenv("email_list")
email_list_dev = os.getenv("email_list_dev")
gmail_pass = os.getenv("gmail_pass")


doors_open = ImageHandler.check_garage_doors_open(root_folder=root_folder)
#time.sleep(300)

if doors_open != None:

    doors_open2 = ImageHandler.check_garage_doors_open(root_folder=root_folder)

    if doors_open == doors_open2:
        EmailHandler.send_email(email_list=email_list, email_list_dev = email_list_dev, gmail_pass=gmail_pass, door_open=doors_open2, root_folder=root_folder)
        #SMSHandler.send_sms(door_open=doors_open2, account_sid=twilio_account_sid, auth_token=twilio_auth_token)