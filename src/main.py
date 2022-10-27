from shared_utils import otp_generator, send_email, verify_otp

receiver_email = input("Enter your email: ")

otp_data = otp_generator()
send_email(otp_data, receiver_email)
verify_otp()
