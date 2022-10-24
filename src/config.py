import os
from dotenv import load_dotenv

load_dotenv()


configs = {
    "OTP_SECRET": os.getenv("OTP_SECRET"),
    "OTP_EXPIRY_TIME": os.getenv("OTP_EXPIRY_TIME"),
    "SMTP_PORT": os.getenv("SMTP_PORT"),
    "SMTP_HOST": os.getenv("SMTP_HOST"),
    "SMTP_USER": os.getenv("SMTP_USER"),
    "SMTP_PASSWORD": os.getenv("SMTP_PASSWORD"),
}
