from django.urls import path

from . import views


urlpatterns = [
    path("phrase/", views.PhraseListView.as_view()),
    path("topicphrase/", views.TopicPhraseListView.as_view()),
]
