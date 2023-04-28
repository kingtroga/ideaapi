from rest_framework import generics

from .models import Annoucement
from .serializers import AnnoucementSerializer

class AnnoucementList(generics.ListCreateAPIView):
    queryset = Annoucement.objects.all()
    serializer_class = AnnoucementSerializer

class AnnoucementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annoucement.objects.all()
    serializer_class = AnnoucementSerializer