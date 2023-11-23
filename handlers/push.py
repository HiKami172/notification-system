from .handler import Handler
from config import PUSHPAD_AUTH_TOKEN, PUSHPAD_PROJECT_ID

import pushpad


class PushHandler(Handler):  # recipient - website url
    def handle(self, request):
        if 'push' not in request.delivery_methods:
            return super().handle(request)
        recipient = request.delivery_methods['push']
        text = request.message
        project = pushpad.Pushpad(
            auth_token=PUSHPAD_AUTH_TOKEN,
            project_id=PUSHPAD_PROJECT_ID
        )
        notification = pushpad.Notification(
            project,
            body=text,
            target_url=recipient,
        )

        notification.broadcast()
        return super().handle(request)
