from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()

class AvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['avatar']

    def update(self, instance, validated_data):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance