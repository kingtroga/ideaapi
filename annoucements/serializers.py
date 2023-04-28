from rest_framework import serializers

from .models import Annoucement

class AnnoucementSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        fields = (
            "id",
            "author",
            "author_name",
            "title",
            "body",
            "created_at",
        )
        model = Annoucement

    def get_author_name(self, obj):
        return obj.author.get_full_name() if obj.author else None