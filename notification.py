from states import State, PendingState
from dataclasses import dataclass, field


@dataclass()
class Notification:
    heading: str = field(default=None)
    body: str = field(default=None)
    delivery_methods: dict[str, str] = field(default_factory=dict)
    state: State = field(default_factory=PendingState)

    def set_state(self, state):
        self.state = state

    def handle(self):
        self.state.handle(self)


@dataclass()
class NotificationBuilder:
    notification: Notification = field(default_factory=Notification)

    def set_heading(self, text):
        self.notification.heading = text
        return self

    def set_body(self, text):
        self.notification.body = text
        return self

    def add_delivery_method(self, delivery_type, address):
        self.notification.delivery_methods[delivery_type] = address
        return self

    def build(self):
        return self.notification
