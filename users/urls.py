from django.urls import path
from .views import (
    CustomLoginView, 
    CustomLogoutView, 
    CustomPasswordResetView, 
    CustomPasswordChangeView, 
    SecurityQuestionView
)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='custom_login'),
    path('logout/', CustomLogoutView.as_view(), name='custom_logout'),
    path('securequestion/<user_id>',SecurityQuestionView.as_view(), name="security_question" ),
    path('password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password/change/<uidb64>/<token>/', CustomPasswordChangeView.as_view(), name='password_change'),
]
