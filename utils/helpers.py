from django.contrib import messages
from django.contrib.sites.models import Site
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from business.forms import BankDetailsForm
from business.models import Business, StaffInvite, TeamMember
from users.models import User
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


def send_team_invite_link(invite_id, email):
    current_site = Site.objects.get_current()

    invite_path = reverse('business:teamInvite', kwargs={'invite_id': invite_id})

    invite_link = '%s%s' % (current_site.domain, invite_path)

    print(invite_link)
    # Mailer(template='business/mail/team/invite.html', subject='Scrow - Invite to join a team', to_email=email,
    #        payload={'invite_link': invite_link})


def check_password_reset_token(user, reset_token):
    token = Token()
    eval_token = token.evaluate_token(user.pk, reset_token)
    token.remove_token(user.pk)

    return eval_token


def update_bank_details(request, form):
    if request.user.business:
        try:
            business = Business.objects.get(pk=request.user.business.pk)
        except Business.DoesNotExist:
            raise Http404

    if business.bank:
        form = BankDetailsForm(instance=business.bank, data=request.POST)
    if form.is_valid():
        bank = form.save()
        if business:
            business.bank = bank
            business.save()
        else:
            user = User.objects.get(pk=request.user.pk)
            user.bank = bank
            user.save()
        messages.success(request, 'Bank details updated!')


def check_username_exist(model, pk, name):
    return model.objects.filter(~Q(id=pk), name=name).exists()


def check_email_exist(model, pk, email):
    return model.objects.filter(~Q(id=pk), email=email).exists()


def check_phone_exist(model, pk, phone):
    return model.objects.filter(~Q(id=pk), phone=phone).exists()


def validate_invite(invite_id, request):
    try:
        invite = StaffInvite.objects.get(invite_id=invite_id)
    except StaffInvite.DoesNotExist:
        return messages.warning(request, 'Invite link not valid.')

    if invite.is_active:
        return messages.warning(request, 'Invite link has already been used, thus is no longer active.')\

    if TeamMember.objects.filter(user=request.user.pk, business=invite.business.pk):
        return messages.warning(request, 'You are already a member of this team.')

    return invite
