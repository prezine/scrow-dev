from django.contrib import admin
from django.urls import path, include

from core.views import homepage_view
from users.views import register_user_view, dashboard_view, LoginView

urlpatterns = [
    path('sudo/admin/ps', admin.site.urls),
    path('', homepage_view, name='homepage'),
    path('register', register_user_view, name='userRegistration'),
    path('login', LoginView.as_view(), name='userLogin'),
    path('api/users/', include('users.urls')),
    path('dashboard', dashboard_view, name='dashboard')
]
