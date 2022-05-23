from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = format_suffix_patterns([
    path("video/", views.VideoViewSet.as_view({'get': 'list'})),
    path("video/<int:pk>", views.VideoViewSet.as_view({'get': 'retrieve'})),
    path("topicvideo/", views.TopicVideoListView.as_view()),
])
