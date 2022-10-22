import pyotp


def otp_generator():
    totp = pyotp.TOTP("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    otp = totp.now()
    return otp
