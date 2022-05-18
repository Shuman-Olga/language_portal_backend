from django.urls import path

from . import views


urlpatterns = [
    path("word/", views.WordListView.as_view()),
    path("topicword/", views.TopicWordListView.as_view()),
    # path("word/<int:pk>", views.WordDetailView.as_view()),
]
