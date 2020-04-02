from django.urls import path
from django.utils.decorators import decorator_from_middleware

from transactions.views import transaction_index_view, NewTransactionView, PaymentView
from utils.auth_middlewares import AuthOnlyMiddleware, BusinessOnlyMiddleware

user_auth_access_decorator = decorator_from_middleware(AuthOnlyMiddleware)
business_only_access_decorator = decorator_from_middleware(BusinessOnlyMiddleware)

app_name = 'transactions'
urlpatterns = [
    path('', user_auth_access_decorator(transaction_index_view), name='index'),
    path('new', business_only_access_decorator(NewTransactionView.as_view())),
    path('payment/<str:transaction_id>', PaymentView.as_view(), name='payment')
]
