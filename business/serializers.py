from rest_framework import serializers

from business.models import Business, Staff, Role, BusinessVerification
from users.models import User


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    userId = serializers.CharField(required=False, allow_blank=True)
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = Business
        exclude = ('staffs',)

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

        if Role.objects.filter(user=user_id).exists():
            raise serializers.ValidationError('Sorry! You cannot create a business as you are already a worker in one.')

        return attrs

    def create(self, validated_data):
        user = User.objects.get(pk=validated_data.get('userId'))
        business = Business.objects.create(
            name=validated_data.get('name'),
            email=validated_data.get('email'),
            country=validated_data.get('country'),
            state=validated_data.get('state'),
            city=validated_data.get('city'),
            address=validated_data.get('address'),
            category=validated_data.get('category'),
            sub_category=validated_data.get('sub_category'),
            website=validated_data.get('website'),
            business_type=validated_data.get('business_type')
        )

        user.business = business
        user.save()
        role = Role.objects.create(role='Owner', user=user)
        Staff.objects.create(role=role, business=business)
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
