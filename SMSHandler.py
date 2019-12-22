from twilio.rest import Client

def send_sms (door_open, account_sid, auth_token, from_sms_number, to_sms_number):

       client = Client(account_sid, auth_token)

       message = client.messages.create(
              from_=from_sms_number,
              body="Oh no! %s doors is/are open." % door_open,
              to=to_sms_numbers,
       )
       print("Sent SMS Alert!")