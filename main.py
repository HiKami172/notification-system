from notification import NotificationBuilder


def main():
    heading = "Heading"
    body = 'message'
    email = 'target_email'
    phone = 'target_phone'  # including plus sign
    builder = NotificationBuilder() \
        .set_heading(heading) \
        .set_body(body) \
        .add_delivery_method('email', email) \
        .add_delivery_method('sms', phone)
    builder.build().handle()


if __name__ == '__main__':
    main()
