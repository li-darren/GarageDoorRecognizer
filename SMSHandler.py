from twilio.rest import Client

def send_sms (door_open, account_sid, auth_token):

       client = Client(account_sid, auth_token)

       message = client.messages.create(
              from_='whatsapp:+14155238886',
              body="Oh no! %s doors is/are open." % door_open,
              to='whatsapp:+16477170038',
       )
       print("Sent SMS Alert!")