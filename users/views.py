from dj_rest_auth.views import LoginView
from .serializers import CustomLoginSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView




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