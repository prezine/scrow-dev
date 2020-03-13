from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from business.forms import BankDetailsForm
from business.models import Business, Staff, StaffInvite
from business.serializers import BusinessSerializer, BusinessVerificationSerializer, StaffSerializer, \
    StaffInviteSerializer
from utils.helpers import update_bank_details, send_team_invite_link
from utils.token import Token, generate_invite_token


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


class TeamMembersView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StaffSerializer

    def get(self, request):
        queryset = Staff.objects.filter(business=request.user.business.pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        try:
            Staff.objects.get(business=request.user.business.pk, role__role='Owner', role__user=request.user.pk)
        except Staff.DoesNotExist:
            return Response(data={'response': 'You do not have the permission to access this area'},
                            status=status.HTTP_401_UNAUTHORIZED)
        data = {
            'name': request.data.get('name'),
            'role': request.data.get('role'),
            'business': request.user.business.pk
        }

        serializer = StaffInviteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        invite_id = generate_invite_token()
        data['invite_id'] = invite_id

        staff_obj, created = StaffInvite.objects.get_or_create(
            business=request.user.business,
            name=request.data.get('name'),
            role=request.data.get('role'),
            defaults={'invite_id': invite_id},
        )

        send_team_invite_link(staff_obj.invite_id)

        return Response(data='Invite sent! Invitee will be added to the team once invite is accepted.')
