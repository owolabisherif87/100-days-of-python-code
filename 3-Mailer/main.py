from email.message import EmailMessage
from email import message_from_string
import os
import smtplib
from email.utils import formataddr
from datetime import datetime


msg = EmailMessage()
msg["subject"] = f"Alert! Alert!! Alert!!! {datetime.now()}"
msg["to"] = "owolabisherif@emqatar.com"
msg["cc"] = "owolabisherif87@gmail.com"
msg["from"] = formataddr(("Office Computer", "office@echomedia.com"))
msg.set_content("Hi Sherif!,\nSomeone just powered up your system.")


with smtplib.SMTP_SSL("webmail.emqatar.com", 465) as smtp:
    try:
        smtp.login('owolabisherif@emqatar.com', 'xxxxx')
        smtp.send_message(msg)
    except smtplib.SMTPAuthenticationError as err:
        print(err)
