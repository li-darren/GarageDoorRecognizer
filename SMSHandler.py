from twilio.rest import Client

def send_sms (door_open, account_sid, auth_token):

       client = Client(account_sid, auth_token)

       message = client.messages.create(
              from_='+12019924112',
              body="Oh no! %s doors is/are open." % door_open,
              to='+16477170038',
       )
       print("Sent SMS Alert!")