from rest_framework import serializers
from .models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('id', 'title', 'body', 'author', 'author_name', 'created_at', )

class AnnouncementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('title', 'body',)

class AnnouncementEditDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('id', 'title', 'body')