import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))


def send_email(to_email: str, subject: str, body: str):

    print("=" * 50)
    print("SMTP_SERVER :", SMTP_SERVER)
    print("SMTP_PORT   :", SMTP_PORT)
    print("SMTP_EMAIL  :", SMTP_EMAIL)
    print("=" * 50)

    message = EmailMessage()

    message["From"] = SMTP_EMAIL
    message["To"] = to_email
    message["Subject"] = subject
    message.set_content(body)

    with smtplib.SMTP_SSL(
        SMTP_SERVER,
        SMTP_PORT,
        timeout=20
    ) as server:

        server.set_debuglevel(1)

        print("Connected to SMTP Server")

        # server.starttls()
        # print("TLS Started")

        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        print("Logged In")

        server.send_message(message)
        print("Email Sent Successfully")


