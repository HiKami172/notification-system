from config import sender_email, email_password
from .handler import Handler

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailHandler(Handler):  # recipient - email

    def handle(self, request):
        if 'email' not in request.delivery_methods:
            return super().handle(request)
        recipient = request.delivery_methods['email']
        text = request.message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient
        message['Subject'] = 'Notification System'
        message.attach(MIMEText(text, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, email_password)
            server.sendmail(sender_email, recipient, message.as_string())
        return super().handle(request)
