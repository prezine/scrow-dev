from django.urls import path
from django.utils.decorators import decorator_from_middleware

from utils.auth_middlewares import BusinessOnlyMiddleware, AuthOnlyMiddleware
from .views import (register_view, CreateBusinessView, BankDetailsView, business_setup, verification_view,
                    bank_details_edit_view, VerificationFileUpload, TeamMembersView, BusinessView, FindUsers,
                    TeamInviteView, switch_business_view, business_verification_details_view)

business_only_access_decorator = decorator_from_middleware(BusinessOnlyMiddleware)
user_auth_access_decorator = decorator_from_middleware(AuthOnlyMiddleware)

app_name = 'business'
urlpatterns = [
    path('register', register_view, name='register'),
    path('create', CreateBusinessView.as_view(), name='create'),

    path('bank-details', business_only_access_decorator(BankDetailsView.as_view()), name='bank_details'),
    path('setup', business_only_access_decorator(business_setup), name='setup'),
    path('bank-verify', business_only_access_decorator(bank_details_edit_view), name='bank_details_form'),
    path('verification', business_only_access_decorator(verification_view), name='verification'),
    path('documents-upload', business_only_access_decorator(VerificationFileUpload.as_view())),
    path('verification_details', business_only_access_decorator(business_verification_details_view)),

    path('team', business_only_access_decorator(TeamMembersView.as_view()), name='workers'),
    path('team/find', business_only_access_decorator(FindUsers.as_view())),
    path('team/invite/<str:invite_id>', user_auth_access_decorator(TeamInviteView.as_view()), name='teamInvite'),

    path('details', BusinessView.as_view()),
    path('switch/<int:pk>', switch_business_view, name='switch')
]
