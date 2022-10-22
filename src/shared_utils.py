import pyotp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import configs


def otp_generator():
    totp = pyotp.TOTP(configs["OTP_SECRET"])
    otp = totp.now()
    return otp


def send_email(otp, receiver_email):
    try:
        # creates SMTP session
        server = smtplib.SMTP("smtp.gmail.com", 587)

        # start TLS for security
        server.starttls()

        # Authentication
        server.login("developer4all36@gmail.com", "vieztopskzocmnlv")

        # message to be sent
        message = MIMEMultipart()
        message["From"] = "TestApp <developer4all36@gmail.com>"
        message["To"] = receiver_email
        message["Subject"] = "Password OTP"
        message.attach(MIMEText(f"Hello there, your OTP: {otp}", "plain"))

        # sending the mail
        server.sendmail(
            "developer4all36@gmail.com", receiver_email, msg=message.as_string()
        )

        print("OTP Sent to your email")

    except Exception:
        raise Exception("An error occurred while sending the email")
