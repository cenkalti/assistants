import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from framework import FunctionToolkit, LLMAssistant

ZOHO_SMTP_EMAIL = os.environ["ZOHO_SMTP_EMAIL"]
ZOHO_SMTP_PASSWORD = os.environ["ZOHO_SMTP_PASSWORD"]


def send_email(to: str, subject: str, body: str):
    """Sends an email to the specified recipient with the given subject and body.

    Args:
        to (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body of the email. It should be in HTML format.
    Returns:
        None
    """
    msg = MIMEMultipart()
    msg["From"] = ZOHO_SMTP_EMAIL
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    with smtplib.SMTP_SSL("smtp.zoho.com", 465) as server:
        server.login(ZOHO_SMTP_EMAIL, ZOHO_SMTP_PASSWORD)
        server.sendmail(msg["From"], msg["To"], msg.as_string())
        server.quit()


email = LLMAssistant(
    name="Email",
    system_prompt="You are an assistant that can send emails",
    toolkit=FunctionToolkit([send_email]),
)
