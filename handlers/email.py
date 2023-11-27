import keys
from .handler import Handler

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailHandler(Handler):  # recipient - email

    def handle(self, request):
        if 'email' not in request.delivery_methods:
            return super().handle(request)
        recipient = request.delivery_methods['email']
        message = MIMEMultipart()
        message['From'] = keys.sender_email
        message['To'] = recipient
        message['Subject'] = request.heading
        message.attach(MIMEText(request.body, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(keys.sender_email, keys.email_password)
            server.sendmail(keys.sender_email, recipient, message.as_string())
        return super().handle(request)
