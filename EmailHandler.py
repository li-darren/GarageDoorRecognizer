import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(email_list, gmail_pass, door_open, root_folder):
    
    jpg_path = root_folder + "/Output Photos/Original_Photo.jpg"

    port = 465  # For SSL
    ssl_context = ssl.create_default_context()

    #this create a multipart message where you can add text and images
    msg = MIMEMultipart()

    msg['From']="garagedoorrecognizer@gmail.com"
    msg['To']=email_list
    msg['Subject']="Garage Door ALERT!!"
    body = "Oh no! %s doors is/are open." % door_open
    msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % (body, "OriginalPhoto"), 'html')  
    msg.attach(msgText)

    try:
        with open(jpg_path, 'rb') as fp:
            img = MIMEImage(fp.read())
            img.add_header('Content-ID', '<{}>'.format("OriginalPhoto"))
            msg.attach(img)
        fp.close()                      
    except IOError:
        print("File not accessible")
    except:
        print("Could not add image")

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=ssl_context) as server:
        server.login("garagedoorrecognizer@gmail.com", gmail_pass)
        server.send_message(msg)
        print("Sent Email Alert!")