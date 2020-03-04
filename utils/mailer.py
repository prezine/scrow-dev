from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class Mailer:
    def __init__(self, template, subject, to_email, payload={}):
        message = render_to_string(template, payload)
        raw_message = strip_tags(message)
        from_email = 'Scrow <noreply@scrow.com>'
        send_mail(subject, raw_message, from_email, [to_email], html_message=message)
