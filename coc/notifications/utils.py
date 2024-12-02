from django.core.mail import send_mail


def send_email_notification(user, subject, message):
    if not user.email:
        raise ValueError("User has no email address.")

    # Send the email
    send_mail(
        subject,
        message,
        'jeremymayaka96@gmail.com',  # From email
        [user.email],  # To email
        fail_silently=False,
    )
