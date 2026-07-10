import os #for read environment variables from .env file
import smtplib #SMTP library - it is responsible for actually connecting with gmail and sendin email
from email.message import EmailMessage #instead of writing ram email text.Python provides EmailMessage object
from dotenv import load_dotenv

load_dotenv()

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")

def send_email(to_email:str, subject:str,body:str):
    message = EmailMessage()

    message["From"] = SMTP_EMAIL
    message["To"] = to_email
    message["Subject"] = subject

    message.set_content(body)

    with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_EMAIL,SMTP_PASSWORD)
        server.send_message(message)


