import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_email_alert():
    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_password = os.getenv("EMAIL_PASSWORD")
    receiver_email = "kb305919@gmail.com"

    if not sender_email or not sender_password:
        print("❌ Email credentials are missing. Check your .env file.")
        return

    msg = MIMEText("🚨 Anomaly detected in fiber optic system!")
    msg["Subject"] = "⚠️ Alert: Fiber Optic Anomaly Detected"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__": 
    send_email_alert()
