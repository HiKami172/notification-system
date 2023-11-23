import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    def __init__(self, sender, password):
        self.sender = sender
        self.password = password

    def send(self, recipient, text, **kwargs):
        message = MIMEMultipart()
        message['From'] = self.sender
        message['To'] = recipient
        message['Subject'] = kwargs.get('subject', 'Notification System')
        message.attach(MIMEText(text, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(self.sender, self.password)
            server.sendmail(self.sender, recipient, message.as_string())
