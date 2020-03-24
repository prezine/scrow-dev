from rest_framework import serializers

from business.models import Business, TeamMember, BusinessVerification, StaffInvite
from users.models import User
from users.serializers import UserSerializer


class TeamMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TeamMember
        fields = '__all__'


class StaffInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffInvite
        exclude = ('invite_id', 'is_active')


class BusinessSerializer(serializers.ModelSerializer):
    userId = serializers.CharField(required=False, allow_blank=True)
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = Business
        fields = '__all__'

    def validate(self, attrs):
        email = attrs.get('email')
        name = attrs.get('name')
        try:
            user_id = int(attrs.get('userId'))
        except ValueError:
            raise serializers.ValidationError('Request could not be validated')

        if Business.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email address already taken.')

        if Business.objects.filter(name=name).exists():
            raise serializers.ValidationError('Business name already in use.')

        if not User.objects.filter(pk=user_id).exists():
            raise serializers.ValidationError('Request could not be validated.')

        return attrs

    def create(self, validated_data):
        user = User.objects.get(pk=validated_data.get('userId'))
        business = Business.objects.create(
            name=validated_data.get('name'),
            email=validated_data.get('email'),
            address=validated_data.get('address'),
            website=validated_data.get('website'),
            description=validated_data.get('description'),
            business_type=validated_data.get('business_type')
        )

        user.active_business = business
        user.save()
        TeamMember.objects.create(role='Owner', user=user, business=business)
        return business


class BusinessVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessVerification
        fields = '__all__'

    def create(self, validated_data):
        verification = BusinessVerification.objects.filter(business=validated_data.get('business').pk)
        if verification:
            verification.update(**validated_data)
            verification = BusinessVerification.objects.get(business=validated_data.get('business').pk)
        else:
            verification = BusinessVerification.objects.create(**validated_data)

        return verification


class BusinessUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = Business
        fields = '__all__'
