from django.urls import path
from . import views


urlpatterns = [
    path("video/", views.VideoListView.as_view()),
    path("topicvideo/", views.TopicVideoListView.as_view()),
    path("video/<int:pk>", views.VideoDetailView.as_view()),
]
