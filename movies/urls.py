from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    path("movie/", views.MovieViewSet.as_view({'get': 'list'})),
    path("movie/<int:pk>", views.MovieViewSet.as_view({'get': 'retrieve'})),
])
