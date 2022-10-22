import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from otp_generator import otp_generator

otp = otp_generator()

receiver_email = input("Enter your email: ")


def send_email():
    # creates SMTP session
    sever = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    sever.starttls()

    # Authentication
    sever.login("developer4all36@gmail.com", "vieztopskzocmnlv")

    # message to be sent
    message = MIMEMultipart()
    message['From'] = "TestApp <developer4all36@gmail.com>"
    message['To'] = receiver_email
    message['Subject'] = "Password OTP"
    message.attach(MIMEText(f"Hello there, your OTP: {otp}", 'plain'))

    # sending the mail
    sever.sendmail("developer4all36@gmail.com", receiver_email, msg=message.as_string())
