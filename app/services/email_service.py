import smtplib
from email.message import EmailMessage

from app.core.config import (
    MAIL_USERNAME,
    MAIL_PASSWORD,
    MAIL_SERVER,
    MAIL_PORT,
    MAIL_FROM_NAME
)


class EmailService:

    @staticmethod
    def send_verification_email(
        email: str,
        verification_link: str
    ):

        message = EmailMessage()

        message["Subject"] = "Verify Your Email"

        message["From"] = (
            f"{MAIL_FROM_NAME} <{MAIL_USERNAME}>"
        )

        message["To"] = email

        message.set_content(
            f"""
Hello,

Click the link below to verify your email.

{verification_link}

Thank You.
"""
        )

        with smtplib.SMTP(
            MAIL_SERVER,
            MAIL_PORT
        ) as smtp:

            smtp.starttls()

            smtp.login(
                MAIL_USERNAME,
                MAIL_PASSWORD
            )

            smtp.send_message(message)

    @staticmethod
    def send_password_reset_email(
        email: str,
        reset_link: str
    ):

        message = EmailMessage()

        message["Subject"] = "Reset Your Password"

        message["From"] = (
            f"{MAIL_FROM_NAME} <{MAIL_USERNAME}>"
        )

        message["To"] = email

        message.set_content(
            f"""
Hello,

Click below to reset your password.

{reset_link}

If you didn't request this,
ignore this email.
"""
        )

        with smtplib.SMTP(
            MAIL_SERVER,
            MAIL_PORT
        ) as smtp:

            smtp.starttls()

            smtp.login(
                MAIL_USERNAME,
                MAIL_PASSWORD
            )

            smtp.send_message(message)