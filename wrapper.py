from dotenv import load_dotenv
import os
import SMSHandler as SMSHandler
import EmailHandler as EmailHandler 

load_dotenv()

twilio_account_sid = os.getenv("account_sid")
twilio_auth_token = os.getenv("auth_token")
email_list = os.getenv("email_list")
gmail_pass = os.getenv("gmail_pass")


