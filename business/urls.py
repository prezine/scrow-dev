from django.urls import path
from django.utils.decorators import decorator_from_middleware

from utils.auth_middlewares import BusinessOnlyMiddleware, AuthOnlyMiddleware
from .views import (register_view, CreateBusinessView, VerificationFileUpload, TeamMembersView, BusinessView, FindUsers,
                    TeamInviteView, switch_business_view, BusinessActivationView)

business_only_access_decorator = decorator_from_middleware(BusinessOnlyMiddleware)
user_auth_access_decorator = decorator_from_middleware(AuthOnlyMiddleware)

app_name = 'business'
urlpatterns = [
    path('register', register_view, name='register'),
    path('create', CreateBusinessView.as_view(), name='create'),

    path('activate', business_only_access_decorator(BusinessActivationView.as_view()), name='activation'),
    path('documents-upload', business_only_access_decorator(VerificationFileUpload.as_view())),

    path('team', business_only_access_decorator(TeamMembersView.as_view()), name='workers'),
    path('team/find', business_only_access_decorator(FindUsers.as_view())),
    path('team/invite/<str:invite_id>', user_auth_access_decorator(TeamInviteView.as_view()), name='teamInvite'),

    path('details', BusinessView.as_view()),
    path('switch/<int:pk>', switch_business_view, name='switch')
]
