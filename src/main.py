from shared_utils import otp_generator, send_email, verify_otp

receiver_email = input("Enter your email: ")

otp = otp_generator()
send_email(otp, receiver_email)
verify_otp(otp)
