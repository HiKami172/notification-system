from .handler import Handler
from config import account_sid, auth_token, phone_number

from twilio.rest import Client


class SMSHandler(Handler):  # recipient - phone number

    def handle(self, request):
        if 'sms' not in request.delivery_methods:
            return super().handle(request)
        recipient = request.recipient
        text = request.message

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=text,
            from_=phone_number,
            to=recipient
        )
        return super().handle(request)

