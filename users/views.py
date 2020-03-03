from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from users.forms import LoginForm
from users.models import User
from users.serializers import UserSerializer


def register_user_view(request):
    return render(request, 'users/register.html')


class RegisterUserApi(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class LoginView(View):
    form_class = LoginForm

    def get(self, request):
        print(request.user)
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'users/login.html', {'form': self.form_class, 'message': []})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email=form.cleaned_data.get('email'))
            except User.DoesNotExist:
                messages.warning(request, 'No user with such credentials exist.')
                return render(request, 'users/login.html', {'form': form, 'message': messages})

            if not user.check_password(form.cleaned_data.get('password')):
                messages.warning(request, 'E-mail address and password does not match.')
                return render(request, 'users/login.html', {'form': form, 'message': messages})

            user = authenticate(username=form.cleaned_data.get('email'), password=form.cleaned_data.get('password'))
            if not user:
                messages.warning(request, 'Request could not be validated. Please reload and try again')
                return render(request, 'users/login.html', {'form': form, 'message': messages})

            if not user.is_active:
                messages.warning(request, 'Login failed! Please contact support for help.')
                return render(request, 'users/login.html', {'form': form, 'message': messages})
            login(request, user)
            return redirect('dashboard')
        return render(request, 'users/login.html', {'form': form, 'message': messages})


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return HttpResponse('<h1>Dashboard</h1>')
