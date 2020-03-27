from django.urls import path

from users.views import RegisterUserApi, ResendVerificationLinkView, ProfileDetailsView, HalfProfileDetailsView

app_name = 'users'

urlpatterns = [
    path('create-user', RegisterUserApi.as_view(), name='user_registration'),
    path('profile-details', ProfileDetailsView.as_view(), name='user_profile'),
    path('half-profile-details', HalfProfileDetailsView.as_view()),
    path('resend-verification-link', ResendVerificationLinkView.as_view()),
]
