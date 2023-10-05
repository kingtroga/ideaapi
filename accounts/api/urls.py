from django.urls import path
from accounts.api.views import (
    registration_view
)
from accounts.api.views import UsersView

urlpatterns = [
    path('signup/', registration_view, name='signup'),
    path('users/', UsersView.as_view(), name='users'),
]