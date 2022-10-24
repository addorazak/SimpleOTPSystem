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
        server = smtplib.SMTP(configs["SMTP_HOST"], configs["SMTP_PORT"])

        # start TLS for security
        server.starttls()

        # Authentication
        server.login(configs["SMTP_USER"], configs["SMTP_PASSWORD"])

        # message to be sent
        message = MIMEMultipart()
        message["From"] = "TestApp " + configs["SMTP_USER"]
        message["To"] = receiver_email
        message["Subject"] = "Password OTP"
        message.attach(MIMEText(f"Hello there, your OTP: {otp}", "plain"))

        # sending the mail
        server.sendmail(configs["SMTP_USER"], receiver_email, msg=message.as_string())

        print("OTP Sent to your email")

    except Exception:
        raise Exception("An error occurred while sending the email")


def verify_otp(otp):
    retries_count = 0
    retries_limit = 2

    while retries_count <= retries_limit:
        received_otp = input("Enter the OTP received: ")
        retries_count += 1
        if received_otp == otp:
            print("Verified")
            break
        else:
            print("Not valid")
    else:
        print("Please request for new otp. \n App exiting...")
