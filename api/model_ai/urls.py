from django.urls import path
from .views import ModelAIView

urlpatterns = [
    path("detect/", ModelAIView.video_feed, name="face-recognition"),
]
