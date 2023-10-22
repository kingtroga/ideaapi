from django.urls import path
from accounts.api.views import (
    registration_view
)
from accounts.api.views import UsersView

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('users/', UsersView.as_view(), name='users'),
]