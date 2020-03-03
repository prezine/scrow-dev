from django.contrib.auth import authenticate, login
from rest_framework import serializers

from users.models import User
from utils.token import Token


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, error_messages={'required': 'username is required.'})
    email = serializers.CharField(error_messages={'required': 'email address is required.'})
    retype_password = serializers.CharField(required=False, allow_blank=True)

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

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email address already taken')

        if User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError('Email address already taken')

        if User.objects.filter(name=name).exists():
            raise serializers.ValidationError('Username already in use')

        return attrs

    def create(self, validated_data):
        instance = User(
            name=validated_data.get('name'),
            email=validated_data.get('email').lower(),
            phone=validated_data.get('phone'),
            country=validated_data.get('country'),
            state=validated_data.get('state'),
            city=validated_data.get('city'),
            address=validated_data.get('address'),
            gender=validated_data.get('gender'),
        )
        instance.set_password(validated_data.get('password').lower())
        instance.save()
        token = Token()
        verification_code = token.gen_token(length=35, ext='alphanum')
        token.persist_token(verification_code, instance.email, lifetime=None)

        user = authenticate(username=instance.email, password=validated_data.get('password').lower())
        login(self.context.get("request"), user)

        print(verification_code)
        return instance
