from shared_utils import otp_generator, send_email

receiver_email = input("Enter your email: ")

otp = otp_generator()
send_email(otp, receiver_email)


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
