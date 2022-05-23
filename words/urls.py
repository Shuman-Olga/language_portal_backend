from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = format_suffix_patterns([
    path("word/", views.WordViewSet.as_view({'get': 'list'})),
    path("word/<int:pk>", views.WordViewSet.as_view({'get': 'retrieve'})),
    # path("word/", views.WordRandomView.as_view()),
    path("topicword/", views.TopicWordListView.as_view()),
    # path("word/<int:pk>", views.WordDetailView.as_view()),
])
