from .handler import Handler
import keys

from twilio.rest import Client


class SMSHandler(Handler):  # recipient - phone number

    def handle(self, request):
        if 'sms' not in request.delivery_methods:
            return super().handle(request)
        recipient = request.delivery_methods['sms']
        text = request.body

        client = Client(keys.account_sid, keys.auth_token)
        message = client.messages.create(
            body=text,
            from_=keys.phone_number,
            to=recipient
        )
        return super().handle(request)

