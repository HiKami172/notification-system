from handlers import email, push, sms
from handlers.handler import Handler


class State:
    def handle(self, notification):
        pass


class PendingState(State):
    def handle(self, notification):
        print(f"Notification pending...\n"
              f"Delivery methods: {notification.delivery_methods}")
        handler = email.EmailHandler().set_next(sms.SMSHandler().set_next(push.PushHandler()))
        try:
            handler.handle(notification)
            notification.set_state(DeliveredState())
        except Exception as e:
            print(e)
            notification.set_state(FailedState())
        notification.handle()


class DeliveredState(State):
    def handle(self, notification):
        print("Notification successfully delivered.")


class FailedState(State):
    def __init__(self, e: Exception):
        self.e = e

    def handle(self, notification):
        print("Encountered error while delivering notification.\n"
              f"{self.e}\n"
              f"Retrying...")
        notification.set_state(PendingState())
        notification.handle()
