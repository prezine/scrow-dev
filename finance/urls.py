from django.urls import path
from django.utils.decorators import decorator_from_middleware

from finance.views import BankDetailsView
from utils.auth_middlewares import BusinessOnlyMiddleware

business_only_access_decorator = decorator_from_middleware(BusinessOnlyMiddleware)

app_name = 'finance'
urlpatterns = [
    path('', business_only_access_decorator(BankDetailsView.as_view())),
]
