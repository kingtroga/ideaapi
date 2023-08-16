from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from .serializers import AvatarSerializer
from rest_framework.response import Response

class ChangeAvatarAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    parser_classes = [FormParser, MultiPartParser]
    

    def post(self, request, format=None):
        user = request.user
        serializer = AvatarSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=200)
        
        else:
            return Response(data=serializer.errors, status=500)