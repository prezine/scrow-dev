from django.urls import path
from django.utils.decorators import decorator_from_middleware

from transactions.views import (transaction_index_view, PaymentView, ProductView, customers_view, customers_api_view,
                                delete_product, update_stock, update_product)
from utils.auth_middlewares import AuthOnlyMiddleware, BusinessOnlyMiddleware

user_auth_access_decorator = decorator_from_middleware(AuthOnlyMiddleware)
business_only_access_decorator = decorator_from_middleware(BusinessOnlyMiddleware)

app_name = 'transactions'
urlpatterns = [
    path('', business_only_access_decorator(transaction_index_view), name='index'),
    path('product', ProductView.as_view()),
    path('customers', customers_api_view),
    path('payment/<str:customer_uid>/<str:product_id>', PaymentView.as_view(), name='payment'),
    path('delete/<int:product_pk>', delete_product, name='delete_product'),
    path('update-stock/<int:product_pk>', update_stock, name='update_stock'),
    path('update-product/<int:product_pk>', update_product, name='update_product')
]
