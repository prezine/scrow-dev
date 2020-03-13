from django.urls import path
from django.utils.decorators import decorator_from_middleware

from utils.auth_middlewares import BusinessOnlyMiddleware
from .views import (register_view, CreateBusinessView, BankDetailsView, business_setup, verification_view,
                    bank_details_edit_view, VerificationFileUpload, TeamMembersView, BusinessView)

business_only_access_decorator = decorator_from_middleware(BusinessOnlyMiddleware)

app_name = 'business'
urlpatterns = [
    path('register', register_view, name='register'),
    path('create', CreateBusinessView.as_view(), name='create'),
    path('bank-details', business_only_access_decorator(BankDetailsView.as_view()), name='bank_details'),
    path('setup', business_only_access_decorator(business_setup), name='setup'),
    path('bank-verify', business_only_access_decorator(bank_details_edit_view), name='bank_details_form'),
    path('verification', business_only_access_decorator(verification_view), name='verification'),
    path('documents-upload', business_only_access_decorator(VerificationFileUpload.as_view())),
    path('team', business_only_access_decorator(TeamMembersView.as_view()), name='workers'),
    path('details', BusinessView.as_view())
]
