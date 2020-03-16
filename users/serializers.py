from django.contrib.auth import authenticate, login
from django.utils import dateparse, timezone
from rest_framework import serializers

from business.models import StaffInvite, Role, Staff
from users.models import User
from utils.helpers import send_verification_link, check_username_exist, check_email_exist, check_phone_exist


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, error_messages={'required': 'username is required.'})
    email = serializers.CharField(error_messages={'required': 'email address is required.'})
    retype_password = serializers.CharField(required=False, allow_blank=True)
    date_of_birth = serializers.CharField(required=True)
    invite_id = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        password = attrs.get('password')
        retype_password = attrs.get('retype_password')
        email = attrs.get('email')
        name = attrs.get('name')
        phone = attrs.get('phone')

        if not password == retype_password:
            raise serializers.ValidationError('Password and retyped password does not match')

        validate_user_existence(serializers, email, phone, name)

        if attrs.get('invite_id'):
            try:
                invite = StaffInvite.objects.get(invite_id=attrs.get('invite_id'))
            except StaffInvite.DoesNotExist:
                raise serializers.ValidationError('Sorry your invite link is not valid')

            if invite.is_active:
                raise serializers.ValidationError('Invite link has already been used, thus is no longer active.')

        return attrs

    def create(self, validated_data):
        date_of_birth = dateparse.parse_datetime(validated_data.get('date_of_birth')).date()

        instance = User(
            name=validated_data.get('name'),
            email=validated_data.get('email').lower(),
            phone=validated_data.get('phone'),
            country=validated_data.get('country'),
            state=validated_data.get('state'),
            city=validated_data.get('city'),
            address=validated_data.get('address'),
            gender=validated_data.get('gender'),
            date_of_birth=date_of_birth,
        )
        instance.set_password(validated_data.get('password').lower())
        instance.save()

        if validated_data.get('invite_id'):
            invite = StaffInvite.objects.get(invite_id=validated_data.get('invite_id'))
            invite.is_active = timezone.now()
            invite.save()

            instance.business = invite.business
            instance.save()

            role = Role.objects.create(role=invite.role, user=instance)
            Staff.objects.create(role=role, business=instance.business)

        user = authenticate(username=instance.email, password=validated_data.get('password').lower())
        login(self.context.get("request"), user)

        send_verification_link(instance)
        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, error_messages={'required': 'username is required.'})
    email = serializers.CharField(error_messages={'required': 'email address is required.'})
    date_of_birth = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'phone', 'calling_code', 'date_of_birth', 'country', 'state', 'city')

    def update(self, instance, validated_data):
        if check_username_exist(User, instance.pk, validated_data.get('name')):
            raise serializers.ValidationError({'non_field_errors': ['Username already in use']})
        elif check_email_exist(User, instance.pk, validated_data.get('email')):
            raise serializers.ValidationError({'non_field_errors': ['Email address already taken']})
        elif check_phone_exist(User, instance.pk, validated_data.get('phone')):
            raise serializers.ValidationError({'non_field_errors': ['Phone number already taken']})

        super().update(instance, validated_data)

        return instance


def validate_user_existence(serializer_reference, email, phone, name, validation_type=None):
    if User.objects.filter(email=email).exists():
        msg = 'Email address already taken'
        if validation_type == 'obj':
            msg = {'non_field_errors': [msg]}
        raise serializer_reference.ValidationError(msg)

    if User.objects.filter(phone=phone).exists():
        msg = 'Phone number already taken'
        if validation_type == 'obj':
            msg = {'non_field_errors': [msg]}
        raise serializer_reference.ValidationError(msg)

    if User.objects.filter(name=name).exists():
        msg = 'Username already in use'
        if validation_type == 'obj':
            msg = {'non_field_errors': [msg]}
        raise serializer_reference.ValidationError(msg)
