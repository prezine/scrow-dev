from django.urls import path

from users.views import RegisterUserApi

app_name = 'users'

urlpatterns = [
    path('create-user', RegisterUserApi.as_view()),
]
