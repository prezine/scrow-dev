from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import View
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from users.forms import LoginForm, ForgotPasswordForm, ForgotResetForm
from users.models import User
from users.serializers import UserSerializer
from utils.helpers import send_verification_link, send_reset_password_link, check_password_reset_token
from utils.token import Token


def register_user_view(request):
    return render(request, 'users/auth/register.html')


class RegisterUserApi(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class LoginView(View):
    form_class = LoginForm

    def get(self, request):
        print(request.user)
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'users/auth/login.html', {'form': self.form_class, 'message': []})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email=form.cleaned_data.get('email'))
            except User.DoesNotExist:
                messages.warning(request, 'No user with such credentials exist.')
                return render(request, 'users/auth/login.html', {'form': form, 'message': messages})

            if not user.check_password(form.cleaned_data.get('password')):
                messages.warning(request, 'E-mail address and password does not match.')
                return render(request, 'users/auth/login.html', {'form': form, 'message': messages})

            user = authenticate(username=form.cleaned_data.get('email'), password=form.cleaned_data.get('password'))
            if not user:
                messages.warning(request, 'Request could not be validated. Please reload and try again')
                return render(request, 'users/auth/login.html', {'form': form, 'message': messages})

            if not user.is_active:
                messages.warning(request, 'Login failed! Please contact support for help.')
                return render(request, 'users/auth/login.html', {'form': form, 'message': messages})
            login(request, user)
            return redirect('dashboard')
        return render(request, 'users/auth/login.html', {'form': form, 'message': messages})


def dashboard_view(request):
    return render(request, 'users/dashboard/index.html')


def account_verification_view(request, verification_code, email):
    if request.user.is_authenticated:
        logout(request)

    token = Token()
    eval_token = token.evaluate_token(email, verification_code)
    token.remove_token(email)

    if eval_token:
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.warning(request, 'Request could not validated.')
            return redirect(reverse('userLogin'))

        if user.is_activated:
            messages.warning(request, 'Account is already been verified')
            return redirect(reverse('userLogin'))

        user.is_activated = timezone.now()
        user.save(update_fields=('is_activated',))

        login(request, user)

        messages.success(request, 'Account activated!.')
        return redirect(reverse('dashboard'))
    messages.warning(request, 'Verification not valid or has expired.')
    return redirect(reverse('userLogin'))


class ResendVerificationLinkView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        if request.user.is_activated:
            return Response({'response': 'Account has already been verified.'}, status=status.HTTP_400_BAD_REQUEST)

        send_verification_link(request.user)
        return Response({'response': 'Verification Link resent!'}, status=status.HTTP_200_OK)


class LostPassword(View):
    form_class = ForgotPasswordForm

    def get(self, request):
        return render(request, 'users/auth/password/lost.html', {'form': self.form_class})

    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            try:
                user = User.objects.get(email=form.cleaned_data.get('email'))
            except User.DoesNotExist:
                messages.warning(request, 'A user with this email address does not exist.')

                return render(request, 'users/auth/password/lost.html', {'form': form})

            send_reset_password_link(user)
            messages.success(request, 'Password reset link has been sent to your email address.')
        return render(request, 'users/auth/password/lost.html', {'form': form})


class PasswordResetView(View):
    form = ForgotResetForm
    form_success = False

    def get(self, request, uidb64=None, reset_token=None):
        if uidb64 is None or reset_token is None:
            raise Http404

        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and check_password_reset_token(user, reset_token):
            return render(request, 'users/auth/password/reset.html',
                          {'success': self.form_success, 'user': user.pk, 'form': self.form})
        else:
            raise Http404

    def post(self, request):
        self.form = self.form(data=request.POST)

        if self.form.is_valid():
            try:
                user = User.objects.get(pk=request.POST['user'])
            except User.DoesNotExist:
                messages.warning(request, 'Request could not be validated.')

                return render(request, 'users/auth/password/reset.html',
                              {'success': self.form_success, 'user': request.POST['user'], 'form': self.form})

            user.set_password(self.form.cleaned_data.get("password").lower())
            user.save()

            self.form_success = True
            messages.success(request, 'Password changed successfully.')

        return render(request, 'users/auth/password/reset.html',
                      {'success': self.form_success, 'user': request.POST['user'], 'form': self.form})


class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect((reverse('homepage')))
