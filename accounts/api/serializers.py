from rest_framework import serializers

from accounts.models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['user_id', 'full_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = CustomUser(
            user_id=self.validated_data['user_id'],
            full_name=self.validated_data['full_name'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': "Passwords must match."})
        user.set_password(password)
        user.save()


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_id', 'full_name']
        