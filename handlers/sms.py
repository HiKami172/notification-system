from twilio.rest import Client


class SMS:
    def __init__(self, account_sid, auth_token, sender):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.sender = sender
        self.client = Client(account_sid, auth_token)

    def send(self, recipient, text):
        message = self.client.messages.create(
            body=text,
            from_=self.sender,
            to=recipient
        )

