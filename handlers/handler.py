class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return self

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)


class EmailHandler(Handler):
    def handle(self, request):
        if request.delivery_method == 'email':
            # send email
            pass
        else:
            return super().handle(request)


class SmsHandler(Handler):
    def handle(self, request):
        if request.delivery_method == 'sms':
            # send sms
            pass
        else:
            return super().handle(request)


class PushNotificationHandler(Handler):
    def handle(self, request):
        if request.delivery_method == 'push':
            # send push notification
            pass
        else:
            return super().handle(request)
