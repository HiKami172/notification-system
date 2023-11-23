from .handler import Handler
from config import cert_file, key_file

# from apns import APNs, Payload


class PushHandler(Handler):  # recipient - device token
    def handle(self, request):
        if 'push' not in request.delivery_methods:
            return super().handle(request)
        return super().handle(request)
        # recipient = request.recipient
        # text = request.message
        # apns = APNs(use_sandbox=True, cert_file=cert_file, key_file=key_file)
        #
        # payload = Payload(alert=text, sound='default', badge=1)
        #
        # apns.gateway_server.send_notification(recipient, payload)
