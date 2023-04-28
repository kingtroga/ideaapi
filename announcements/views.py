from rest_framework import generics

from .permissions import IsAuthorOrReadOnly, IsStaff
from .serializers import AnnouncementSerializer
from .models import Announcement

class AnnouncementCreateView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    permission_classes = (IsStaff,)
    serializer_class = AnnouncementSerializer

class AnnouncementList(generics.ListAPIView):
    queryset = Announcement.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = AnnouncementSerializer

class AnnouncementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = AnnouncementSerializer
