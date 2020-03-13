from django.shortcuts import render


def homepage_view(request):
    return render(request, 'core/index.html')


def settings_view(request):
    return render(request, 'users/settings/index.html')
