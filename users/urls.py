from django.urls import path

from users.views import RegisterUserApi, ResendVerificationLinkView

app_name = 'users'

urlpatterns = [
    path('create-user', RegisterUserApi.as_view(), name='user_registration'),
    path('resend-verification-link', ResendVerificationLinkView.as_view())
]
