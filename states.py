from handlers import email, push, sms
from handlers.handler import Handler


class State:
    def handle(self, notification):
        pass


class PendingState(State):
    def handle(self, notification):
        print(f"Message pending...\n"
              f"Delivery methods: {notification.delivery_methods}")
        handler = email.EmailHandler().set_next(sms.SMSHandler().set_next(push.PushHandler()))
        try:
            handler.handle(notification)
        except:
            notification.set_state(FailedState())
        notification.set_state(DeliveredState())


class DeliveredState(State):
    def handle(self, notification):
        print("Message successfully delivered.")


class FailedState(State):
    def handle(self, notification):
        print("Error while delivering message.\n"
              "Retrying...")
        notification.set_state(PendingState())
