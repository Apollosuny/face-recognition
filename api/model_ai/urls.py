from django.urls import path
from .views import video_feed, toggle_camera

urlpatterns = [
    path("detect/", video_feed, name="face-recognition"),
    path("toggle_camera/", toggle_camera, name="toggle_camera"),
]
