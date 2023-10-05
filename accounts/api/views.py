from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions

from accounts.api.serializers import UserRegistrationSerializer
from accounts.api.serializers import UsersSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully registered a new user'
            data['user_id'] = request.data['user_id']
            data['full_name'] = request.data['full_name']
        else:
            data = serializer.errors
        return Response(data)
    

class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (permissions.IsAuthenticated,)

