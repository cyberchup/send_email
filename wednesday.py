# This is a simple Python Script to let all your friends know it is Wednesday

import smtplib
import ssl
from email.message import EmailMessage

# Feel free to change subject and body to say something different
subject = "It is Wednesday My Dudes"
body = "It is Wednesday My Dudes"

# Sender email should be your gmail account (need to turn off 2FA and enable Less Secure Apps). Receiver email is who the email is being sent to; you can add more emails with a comma.
sender_email = "sender@gmail.com"
receiver_email = "receiver1@gmail.com", "receiver2@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

# When you run the script in the terminal you will be asked to provide the password for the sender email.
print("Sending Email...")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("Email Sent!")