import math
import random as r
import smtplib
import ssl

digits = "0123456789"
OTP = ""

for i in range(6):
    OTP += digits[math.floor(r.random()*10)]

otp = OTP + " is your OTP"

msg = otp

port = 465
email_id = input("Enter your email address: ")
password = input("Type your password and press enter: ")


context = ssl.create_default_context()

with smtplib.SMTP_SSL(email_id, port, context=context) as server:
    server.login(email_id, password)

server.sendmail(email_id, msg)

a = input("Enter Your OTP >>: ")

if a == OTP:
    print("Verified")
else:
    print("Not valid")
