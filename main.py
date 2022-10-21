import pyotp
import smtplib

receiver_email = input("Enter your email: ")

totp = pyotp.TOTP("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

otp = totp.now()

# creates SMTP session
sever = smtplib.SMTP('smtp.gmail.com', 25)

# start TLS for security
sever.starttls()

# Authentication
sever.login("developer4all36@gmail.com", "vieztopskzocmnlv")


# message to be sent
message = f"Hello there, your OTP: {otp}"


# sending the mail
sever.sendmail("developer4all36@gmail.com", receiver_email, message)


# terminating the session
sever.quit()
