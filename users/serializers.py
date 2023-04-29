from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

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