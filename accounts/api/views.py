from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from accounts.api.serializers import RegistrationSerializer

@api_view(['POST',])
@authentication_classes([])
@permission_classes([AllowAny])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "successfully registered a new user."
            data['fullName'] = user.fullName
            data['userID'] = user.userID
        else:
            data = serializer.error
        return Response(data)
