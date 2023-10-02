from django.urls import path
from accounts.api.views import (
    registration_view
)

urlpatterns = [
    path('signup/', registration_view, name='signup'),
]