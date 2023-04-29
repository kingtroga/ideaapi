from django.urls import path
from .views import (
    AnnouncementDetail,
    AnnouncementList,
    AnnouncementCreateView,
    AnnouncementEditDetail,
)

urlpatterns = [
    path("<int:pk>/", AnnouncementDetail.as_view(), name="announcement_detail"),
    path('', AnnouncementList.as_view(), name="announcement_list"),
    path('announcements/create/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('announcements/<int:id>/', AnnouncementEditDetail.as_view(), name='announcement-detail'),
]
