import os
import requests
from dotenv import load_dotenv

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")


def send_email(to_email: str, subject: str, body: str):

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    payload = {
        "sender": {
            "name": "SmartCRM",
            "email": "000najmulhuda@gmail.com"
        },
        "to": [
            {
                "email": to_email
            }
        ],
        "subject": subject,
        "textContent": body
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=20
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)