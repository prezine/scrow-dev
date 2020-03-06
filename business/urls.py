from django.urls import path

from .views import (register_view, CreateBusinessView, BankDetailsView, business_setup, verification_view,
                    bank_details_edit_view, VerificationFileUpload)

app_name = 'business'
urlpatterns = [
    path('register', register_view, name='register'),
    path('create', CreateBusinessView.as_view(), name='create'),
    path('bank-details', BankDetailsView.as_view(), name='bank_details'),
    path('setup', business_setup, name='setup'),
    path('bank-verify', bank_details_edit_view, name='bank_details_form'),
    path('verification', verification_view, name='verification'),
    path('documents-upload', VerificationFileUpload.as_view()),
]
