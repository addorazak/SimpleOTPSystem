import pyotp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import configs
from datetime import datetime

# if the variable is not set, set the default time to 92s
if not configs["OTP_EXPIRY_TIME"]:
    configs["OTP_EXPIRY_TIME"] = 90

# generate a random otp that expires after a certain amount of time set in OTP_EXPIRE_TIME
totp = pyotp.TOTP(configs["OTP_SECRET"], interval=configs["OTP_EXPIRY_TIME"])


def otp_generator():
    otp = totp.now()
    # get time remaining in seconds for otp to expire
    time_remaining = int(totp.interval - datetime.now().timestamp() % totp.interval)
    return {
        "code": otp,
        "expire": time_remaining,
    }


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

        email_content = f"""Hello there, your OTP: {otp["code"]} and expires in {otp["expire"]} seconds"""

        message.attach(MIMEText(email_content, "plain"))

        # sending the mail
        server.sendmail(configs["SMTP_USER"], receiver_email, msg=message.as_string())

        print("OTP Sent to your email")

    except Exception:
        print("An error occurred while sending the email")


def verify_otp():
    retries_count = 0
    retries_limit = 2

    while retries_count <= retries_limit:
        received_otp = input("Enter the OTP received: ")
        retries_count += 1

        if totp.verify(received_otp):
            print("Verified")
            break
        else:
            print("Not valid or otp may have expired")
    else:
        print("Please request for new otp. \n App exiting...")
