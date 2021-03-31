import smtplib
from email.message import EmailMessage


def send_mail(name, email, message):
    new_message = message
    msg = EmailMessage()
    msg['Subject'] = email
    msg['From'] = name
    msg['To'] = 'example@gmail.com'
    msg.set_content(new_message)  

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('example@gmail.com', 'password')
        smtp.send_message(msg)