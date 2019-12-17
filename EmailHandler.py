import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(email_list, email_list_dev, gmail_pass, door_open, root_folder):
    
    og_img_path = root_folder + "/OutputPhotos/Original_Photo.jpg"
    hsv_photo_path = root_folder + "/OutputPhotos/HSV_Photo.jpg"
    mask_photo_path = root_folder + "/OutputPhotos/Mask_Photo.jpg"

    port = 465  # For SSL
    ssl_context = ssl.create_default_context()

    ##########
    ##Create User Friendly Message
    #########
    msg = MIMEMultipart()
    msg['From']="garagedoorrecognizer@gmail.com"
    msg['To']=email_list
    msg['Subject']="Garage Door ALERT!!"
    body = "Oh no! %s doors is/are open." % door_open
    msgHTML = '<b>%s</b><br><img src="cid:%s"><br>' % (body, "OriginalPhoto")

    ##########
    ##Create Dev Message
    #########
    msg_dev = MIMEMultipart()
    msg_dev['From']="garagedoorrecognizer@gmail.com"
    msg_dev['To']=email_list_dev
    msg_dev['Subject']="Garage Door ALERT DEV!!"
    body_dev = "Oh no! %s doors is/are open." % door_open
    msgHTML_dev = '<b>%s</b><br><img src="cid:%s"><br><img src="cid:%s"><br><img src="cid:%s"><br>' % (body_dev, "OriginalPhoto", "HSVPhoto", "MaskPhoto")

    try:
        with open(og_img_path, 'rb') as fp:
            img = MIMEImage(fp.read())
            img.add_header('Content-ID', '<{}>'.format("OriginalPhoto"))
            msg.attach(img)
            msg_dev.attach(img)
            fp.close()
    except IOError:
        print("File not accessible")
        msgHTML += "<b>Picture file does not exist and could not be attached</b><br>"
        msgHTML_dev += "<b>Picture file does not exist and could not be attached</b><br>"
    except:
        print("Could not add image")
        msgHTML += "<b>Could not attach image</b><br>"
        msgHTML_dev += "<b>Could not attach image</b><br>"
    finally:
        msg.attach(MIMEText(msgHTML, 'html'))

    try:
        #########################
        ##Dev only images
        #########################

        with open(hsv_photo_path, 'rb') as fp1:
            img1 = MIMEImage(fp1.read())
            img1.add_header('Content-ID', '<{}>'.format("HSVPhoto"))
            msg_dev.attach(img1)
            fp1.close()

        with open(mask_photo_path, 'rb') as fp2:
            img2 = MIMEImage(fp2.read())
            img2.add_header('Content-ID', '<{}>'.format("MaskPhoto"))
            msg_dev.attach(img2)
            fp2.close()

    except IOError:
        print("Dev File not accessible")
        msgHTML_dev += "<b>Dev Picture file does not exist and could not be attached</b><br>"
    except:
        print("Could not add Dev image")
        msgHTML_dev += "<b>Could not attach dev image</b><br>"
    finally:
        msg_dev.attach(MIMEText(msgHTML_dev, 'html'))


    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=ssl_context) as server:
        server.login("garagedoorrecognizer@gmail.com", gmail_pass)
        server.send_message(msg)
        server.send_message(msg_dev)
        print("Sent Email Alert!")