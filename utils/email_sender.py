import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()
app_password = os.environ["APP_PASSWORD"]
sender_email = os.environ["SENDER_EMAIL"]


def send_email(receiver_email:str,subject:str,content:str) -> str:
    """send an email to the receiver with the given subject and content"""

# Create the email
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(content)

    # Send it
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()                  # Secure the connection
        server.login(sender_email, app_password)
        server.send_message(msg)
    
    print("Email sent successfully")

if __name__ == "__main__":
    send_email(receiver_email="4mh23cs023@gmail.com",subject="Hello from python",content="This is email was sent using python")   