from apns import APNs, Payload

# Path to your APNs certificate and key files
cert_file = 'path_to_your_certificate.pem'
key_file = 'path_to_your_key.pem'
class PushHa:
    def __init__(self):

apns = APNs(use_sandbox=True, cert_file=cert_file, key_file=key_file)

# Device token obtained from the iOS app
device_token = 'device_token'

# Notification payload
payload = Payload(alert='Test Notification', sound='default', badge=1)

# Send the notification
apns.gateway_server.send_notification(device_token, payload)

print('Notification sent successfully to APNs')