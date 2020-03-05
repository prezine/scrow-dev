from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from business.serializers import BusinessSerializer


def register_view(request):
    return render(request, 'business/register.html')


class CreateBusinessView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BusinessSerializer
