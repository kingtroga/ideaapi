from django.urls import path 

from .views import AnnoucementList, AnnoucementDetail

urlpatterns = [
    path(
    "<int:pk>/", AnnoucementDetail.as_view(), name="annoucement_detail"
        ),
    path("", AnnoucementList.as_view(), name="annoucement_list"),
]