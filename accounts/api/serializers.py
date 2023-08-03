from rest_framework import serializers

from accounts.models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['userID', 'fullName', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = CustomUser(
            userID=self.validated_data['userID'],
            fullName=self.validated_data['fullName'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': "Password must match."})
        
        user.set_password(password)
        user.save()
        return user