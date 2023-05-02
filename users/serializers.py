from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from accounts.models import CustomUser


class CustomLoginSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})

    def validate(self, attrs):
        user_id = attrs.get('user_id')
        password = attrs.get('password')

        if user_id and password:
            user = authenticate(request=self.context.get('request'),
                                user_id=user_id, password=password)
            if user:
                attrs['user'] = user
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "user_id" and "password".')
            raise serializers.ValidationError(msg)

        return attrs

class CustomLogoutSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    password = serializers.CharField()


class CustomPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    secure_question = serializers.CharField(max_length=255, required=True)
    secureQusAns = serializers.CharField(max_length=255, required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        secure_question = attrs.get('secure_question')
        secureQusAns = attrs.get('secureQusAns')

        if not email:
            raise serializers.ValidationError('Email is required')

        user = CustomUser.objects.filter(email=email).first()
        if user is None:
            raise serializers.ValidationError('User does not exist')

        if user.security_question != secure_question:
            raise serializers.ValidationError('Incorrect security question')

        attrs['user'] = user
        return attrs

from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

class CustomPasswordChangeSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(max_length=128, write_only=True)
    confirm_new_password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, attrs):
        uidb64 = attrs.get('uidb64')
        token = attrs.get('token')
        new_password = attrs.get('new_password')
        confirm_new_password = attrs.get('confirm_new_password')

        if not uidb64 or not token:
            raise serializers.ValidationError('uidb64 and token are required')

        if new_password != confirm_new_password:
            raise serializers.ValidationError('Passwords do not match')

        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is None or not default_token_generator.check_token(user, token):
            raise serializers.ValidationError('Invalid reset token')

        attrs['user'] = user
        return attrs

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ('email','user_id', 'username', 'password', 'full_name', 'department', 'program', 'security_question', 'secureQusAns', 'is_staff', 'is_doctor')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
