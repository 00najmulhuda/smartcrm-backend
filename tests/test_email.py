from app.services.email_utils import send_email

send_email(
    to_email="000najmulhuda@gmail.com",
    subject="FastAPI test ",
    body="Congratulations! Email service is working."
)

print("email sent successfully")