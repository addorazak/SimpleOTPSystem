import pyotp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

receiver_email = input("Enter your email: ")

totp = pyotp.TOTP("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

otp = totp.now()

# creates SMTP session
sever = smtplib.SMTP('smtp.gmail.com', 587)  # default smtp port for gmail is 587 not 25

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
sever.sendmail("developer4all36@gmail.com", receiver_email,msg=message.as_string())

print("OTP Sent to your email")

#  also app shouldn't quit when the otp is sent... more things to do 

# terminating the session
sever.quit()
