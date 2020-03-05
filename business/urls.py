from django.urls import path

from .views import register_view, CreateBusinessView

app_name = 'business'
urlpatterns = [
    path('register', register_view, name='register'),
    path('create', CreateBusinessView.as_view(), name='create'),
]
