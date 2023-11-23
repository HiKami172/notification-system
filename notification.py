from states import PendingState


class Notification:
    def __init__(self):
        self.message = None
        self.delivery_methods = {}
        self.state = PendingState()

    def set_state(self, state):
        self.state = state

    def handle_request(self):
        self.state.handle(self)


class NotificationBuilder:
    def __init__(self):
        self.notification = Notification()

    def set_message(self, message):
        self.notification.message = message
        return self

    def set_delivery_method(self, delivery_type, address):
        self.notification.delivery_methods[delivery_type] = address
        return self

    def build(self):
        return self.notification
