from dj_rest_auth.views import LoginView
from .serializers import (
    CustomLoginSerializer,
    CustomPasswordResetSerializer, 
    CustomPasswordResetSerializer, 
    CustomPasswordChangeSerializer,
    UserRegistrationSerializer
    )
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from accounts.models import CustomUser
from rest_framework import generics, status
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.response import Response
from rest_framework import serializers


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer

class CustomLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # delete token from database
        Token.objects.get(user=request.user).delete()
        # return success response
        return Response({'success': 'Successfully logged out.'})

class SecurityQuestionView(APIView):
    def get(self, request, user_id):
        try:
            user = CustomUser.objects.get(user_id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        data = {'security_question': user.security_question}
        return Response(data)

class CustomPasswordResetView(generics.GenericAPIView):
    serializer_class = CustomPasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        secureQusAns = serializer.validated_data['secureQusAns']

        if not user.check_answer(secureQusAns):
            raise serializers.ValidationError('Incorrect answer')

        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        return Response({'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)




class CustomPasswordChangeView(generics.GenericAPIView):
    serializer_class = CustomPasswordChangeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        uidb64 = serializer.validated_data['uidb64']
        token = serializer.validated_data['token']
        new_password = serializer.validated_data['new_password']
        confirm_new_password = serializer.validated_data['confirm_new_password']

        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if new_password != confirm_new_password:
                raise serializers.ValidationError('Passwords do not match')

            user.set_password(new_password)
            user.save()

            return Response({'detail': 'Password changed successfully'}, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid reset token'}, status=status.HTTP_400_BAD_REQUEST)