from django.contrib import messages
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, GenericAPIView
from django.views import View

from business.forms import BankDetailsForm
from business.models import Business
from business.serializers import BusinessSerializer, BusinessVerificationSerializer
from utils.helpers import update_bank_details


def register_view(request):
    return render(request, 'business/register.html')


class CreateBusinessView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BusinessSerializer


class BankDetailsView(View):
    form_class = BankDetailsForm

    def get(self, request):
        return render(request, 'business/bank.html', {'form': self.form_class, 'message': messages})

    def post(self, request):
        form = BankDetailsForm(instance=request.user.bank, data=request.POST)
        update_bank_details(request, form)
        return render(request, 'business/bank.html', {'form': form, 'message': messages})


def business_setup(request):
    return render(request, 'business/setup.html')


def bank_details_edit_view(request):
    if request.method == 'POST':
        form = BankDetailsForm(instance=request.user.bank, data=request.POST)
        update_bank_details(request, form)
        return render(request, 'business/setup.html', {'form': form, 'message': messages})
    else:
        return reverse('dashboard')


def verification_view(request):
    return render(request, 'business/verification.html')


class VerificationFileUpload(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BusinessVerificationSerializer
