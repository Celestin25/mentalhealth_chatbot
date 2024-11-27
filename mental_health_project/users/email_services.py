import threading
from django.conf import settings
from users.tokens import generate_token
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        # super().__init__(self)
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=True)


generate_email_message = lambda user_first_name: f"""
Hi {user_first_name},
Welcome to e-health

"""


class EmailService:
    def send_welcome_email(self, user):
        subject = ""
        message = generate_email_message(user.first_name)
        welcome_email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        EmailThread(welcome_email).start()

    def send_account_verification_email(self, request, user):
        current_site = get_current_site(request)
        email_confirmation_subject = ""
        email_confirmation_message = render_to_string('email_confirmation.html', {
            'name': user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        })

        email = EmailMessage(
            email_confirmation_subject,
            email_confirmation_message,
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        EmailThread(email).start()
