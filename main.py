from notification import NotificationBuilder


def main():
    message = 'test message'
    email = 'recipient'
    builder = NotificationBuilder() \
        .set_message(message) \
        .set_delivery_method('email', email)
    notification = builder.build()
    notification.handle_request()


if __name__ == '__main__':
    main()
