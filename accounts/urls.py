from django.urls import path
from .views import ChangeAvatarAPIView

urlpatterns = [
    path('avatar/', ChangeAvatarAPIView.as_view(), name='change_avatar_api_view')
]