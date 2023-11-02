# step1: Get ISS data from web using requests module and ISS API
# step2: Get sunrise and sunset data from web using API
# step3: Send mail using smtplib if time is before noon.

import requests
import smtplib
import email


def send_email(sender, recipient, subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create an SMTP object
    smtp_obj = smtplib.SMTP(smtp_server, smtp_port)

    # Start TLS encryption
    smtp_obj.starttls()

    # Login to the SMTP server
    password = "hkch hpst bfpw ceke"
    smtp_obj.login(sender, password)

    # Create a MIME message object
    msg = email.message.EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)

    # Send the email
    smtp_obj.send_message(msg)

    # Quit the SMTP session
    smtp_obj.quit()


response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.json()['iss_position'])

#today = dt.datetime.now()
sender1 = "mohankramu@gmail.com"
recipient1 = "mohan_21688@yahoo.co.in"
subject1 = "Test email"
body1 = "This is a test email. Latitude is " + \
        (response.json()['iss_position']['latitude']) + ".\n" +\
        "Longitude is " + (response.json()['iss_position']["longitude"])

send_email(sender1, recipient1, subject1, body1)


