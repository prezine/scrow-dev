from django.contrib import messages
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from business.forms import BankDetailsForm
from business.models import TeamMember, StaffInvite, Business, BusinessVerification
from business.serializers import (BusinessSerializer, BusinessVerificationSerializer, TeamMemberSerializer,
                                  StaffInviteSerializer, BusinessUpdateSerializer)
from users.models import User
from users.serializers import UserSerializer
from utils.helpers import send_team_invite_link, validate_invite
from utils.token import generate_invite_token


def register_view(request):
    return render(request, 'business/register.html')


class CreateBusinessView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BusinessSerializer


def business_setup(request):
    return render(request, 'business/setup.html')


def verification_view(request):
    return render(request, 'business/verification.html')


class VerificationFileUpload(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BusinessVerificationSerializer


class TeamMembersView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TeamMemberSerializer

    def get(self, request):
        queryset = TeamMember.objects.filter(business=request.user.active_business.pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        try:
            TeamMember.objects.get(business=request.user.active_business.pk, role='Owner',
                                   user=request.user.pk)
        except TeamMember.DoesNotExist:
            return Response(data={'response': 'You do not have the permission to access this area'},
                            status=status.HTTP_401_UNAUTHORIZED)
        data = {
            'role': request.data.get('role'),
            'email': request.data.get('email'),
            'business': request.user.active_business.pk
        }

        serializer = StaffInviteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        invite_id = generate_invite_token()
        data['invite_id'] = invite_id

        staff_obj, created = StaffInvite.objects.get_or_create(
            business=request.user.active_business,
            email=request.data.get('email'),
            role=request.data.get('role'),
            defaults={'invite_id': invite_id},
        )

        send_team_invite_link(staff_obj.invite_id, email=request.data.get('email'))

        return Response(data='Invite sent! Invitee will be added to the team once invite is accepted.')


class BusinessView(RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BusinessUpdateSerializer

    def get_object(self):
        if self.request.user.active_business:
            try:
                TeamMember.objects.get(business=self.request.user.active_business.pk, role='Owner',
                                       user=self.request.user.pk)
            except TeamMember.DoesNotExist:
                raise Http404

            return self.request.user.active_business
        raise Http404


class FindUsers(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request):
        email = request.GET.get('email')
        team_users = []

        if email:
            team_members = TeamMember.objects.filter(business=request.user.active_business.pk)
            for member in team_members:
                users = User.objects.filter(~Q(pk=member.user.pk), Q(email__contains=email))
                for user in users:
                    team_users.append(user)

        serializer = self.serializer_class(team_users, many=True)
        return Response(data=serializer.data)


class TeamInviteView(View):
    def get(self, request, invite_id):
        validate_invite(invite_id, request)

        return render(request, 'business/team/index.html', {'invite_id': invite_id})

    def post(self, request, invite_id):
        invite_instance = validate_invite(invite_id, request)

        if invite_instance:
            invite_instance.is_active = timezone.now()
            invite_instance.save()

            user = User.objects.get(pk=request.user.pk)
            user.active_business = invite_instance.business
            user.save()

            TeamMember.objects.create(user=user, business=user.active_business, role=invite_instance.role)

            messages.success(request, 'You are now a member of the team.')
        return render(request, 'business/team/index.html', {'invite_id': invite_id})


def switch_business_view(request, pk):
    try:
        business = Business.objects.get(pk=pk)
    except Business.DoesNotExist:
        return redirect(reverse('dashboard'))

    if not TeamMember.objects.filter(user=request.user.pk, business=business.pk):
        return redirect(reverse('dashboard'))

    user = User.objects.get(pk=request.user.pk)
    user.active_business = business
    user.save()

    return redirect(reverse('dashboard'))


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def business_verification_details_view(request):
    try:
        queryset = BusinessVerification.objects.get(business=request.user.active_business.pk)
    except BusinessVerification.DoesNotExist:
        return Response(data={})

    serializer = BusinessVerificationSerializer(instance=queryset)
    return Response(data=serializer.data)


def setup_business(request):
    return render(request, 'business/create.html')


def business_activation(request):
    return render(request, 'business/activation.html')
