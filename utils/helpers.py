from django.contrib.sites.models import Site
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from utils.mailer import Mailer
from utils.token import Token


def send_verification_link(user):
    token = Token()
    verification_code = token.gen_token(length=55, ext='alphanum')
    token.persist_token(verification_code, user.email, lifetime=None)

    current_site = Site.objects.get_current()

    verification_link_path = reverse('accountVerification',
                                     kwargs={'verification_code': verification_code, 'email': user.email})
    verification_link = '%s%s' % (current_site.domain, verification_link_path)

    print(verification_link)
    # Mailer(template='users/mail/verification.html', subject='Scrow Account Verification', to_email=user.email,
    #        payload={'verification_link': verification_link})


def send_reset_password_link(user):
    token = Token()
    reset_token = token.gen_token(length=70, ext='alphanum')
    token_lifetime = 1800

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token.persist_token(reset_token, user.pk, lifetime=token_lifetime)
    current_site = Site.objects.get_current()

    reset_path = reverse('passwordReset',
                         kwargs={'reset_token': reset_token, 'uidb64': uid})
    reset_link = '%s%s' % (current_site.domain, reset_path)

    print(reset_link)
    # Mailer(template='users/mail/password/reset.html', subject='Scrow - Password Reset Request', to_email=user.email,
    #        payload={'reset_link': reset_link})


def check_password_reset_token(user, reset_token):
    token = Token()
    eval_token = token.evaluate_token(user.pk, reset_token)
    token.remove_token(user.pk)

    return eval_token
