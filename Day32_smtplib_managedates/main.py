import smtplib
import email
import datetime as dt


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


if __name__ == "__main__":
    today = dt.datetime.now()
    sender1 = "mohankramu@gmail.com"
    recipient1 = "mohan_21688@yahoo.co.in"
    subject1 = "Test email"
    body1 = "This is a test email. Today is " + today.date()

    send_email(sender1, recipient1, subject1, body1)
