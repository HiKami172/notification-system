class NotificationBuilder:
    def __init__(self):
        self.notification = Notification()

    def set_message(self, message):
        self.notification.message = message
        return self

    def set_recipient(self, recipient):
        self.notification.recipient = recipient
        return self

    def set_delivery_method(self, delivery_method):
        self.notification.delivery_method = delivery_method
        return self

    def build(self):
        return self.notification
