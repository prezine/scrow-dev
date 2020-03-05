from django.contrib import admin
from django.urls import path, include
from django.utils.decorators import decorator_from_middleware

from core.views import homepage_view
from users.views import (register_user_view, dashboard_view, LoginView, account_verification_view,
                         ResendVerificationLinkView, PasswordResetView, LostPassword, LogoutView)
from utils.auth_middlewares import AuthOnlyMiddleware, AuthUserOnlyMiddleware, NonAuthMiddleware

user_auth_access_decorator = decorator_from_middleware(AuthOnlyMiddleware)
non_admin_auth_access_decorator = decorator_from_middleware(AuthUserOnlyMiddleware)
non_auth_access_decorator = decorator_from_middleware(NonAuthMiddleware)

urlpatterns = [
    path('sudo/admin/ps', admin.site.urls),
    path('', homepage_view, name='homepage'),

    path('register', register_user_view, name='userRegistration'),
    path('login', LoginView.as_view(), name='userLogin'),
    path('account-verification/<str:verification_code>/<str:email>', account_verification_view,
         name='accountVerification'),
    path('resend-verification-link', user_auth_access_decorator(ResendVerificationLinkView.as_view()),
         name='resendVerificationLink'),
    path('lost-password', LostPassword.as_view(), name='lostPassword'),
    path('password-reset/<str:reset_token>/<str:uidb64>',
         PasswordResetView.as_view(), name='passwordReset'),
    path('password-reset', PasswordResetView.as_view(), name='password_reset_form'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('api/users/', include('users.urls')),
    path('dashboard', user_auth_access_decorator(dashboard_view), name='dashboard'),

    path('business/', include('business.urls')),
]
