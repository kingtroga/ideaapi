from rest_framework import generics
from accounts.models import CustomUser
from .serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
