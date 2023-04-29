from rest_framework import generics

from .permissions import IsAuthorOrReadOnly, IsStaff, IsAuthor
from .serializers import (
    AnnouncementSerializer, 
    AnnouncementCreateSerializer,
    AnnouncementEditDetailSerializer,
)

from .models import Announcement

class AnnouncementCreateView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    permission_classes = (IsStaff,)
    serializer_class = AnnouncementCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, author_name=self.request.user.full_name)

class AnnouncementList(generics.ListAPIView):
    queryset = Announcement.objects.all()
    #permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = AnnouncementSerializer

class AnnouncementDetail(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()
    #permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = AnnouncementSerializer

class AnnouncementEditDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    permission_classes = (IsAuthor,)
    serializer_class = AnnouncementEditDetailSerializer
    lookup_field = 'id'
