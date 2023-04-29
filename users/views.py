from rest_framework import generics
from dj_rest_auth.views import LoginView
from .serializers import CustomLoginSerializer, CustomLogoutSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from accounts.models import CustomUser
from django.contrib.auth import authenticate



class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer

class CustomLogoutView(generics.GenericAPIView):
    serializer_class = CustomLogoutSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.validated_data['user_id']
        password = serializer.validated_data['password']
        try:
            user = authenticate(request, user_id=user_id, password=password)
            if user is not None:
                # delete token from database
                Token.objects.get(user=user).delete()
                # return success response
                return Response({'success': 'Successfully logged out.'})
            else:
                # return error response
                return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        except CustomUser.DoesNotExist:
            # return error response
            return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
