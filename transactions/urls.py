from django.urls import path
from django.utils.decorators import decorator_from_middleware

from transactions.views import transaction_index_view
from utils.auth_middlewares import AuthOnlyMiddleware

user_auth_access_decorator = decorator_from_middleware(AuthOnlyMiddleware)

app_name = 'transactions'
urlpatterns = [
    path('', user_auth_access_decorator(transaction_index_view), name='index'),
]
