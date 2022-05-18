from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from .service import MovieFilter
from .models import Movie
from .serializers import MovieDetailSerializer, MovieListSerializer


class MovieListView(generics.ListAPIView):
    """Вывод списка фильмов"""
    queryset = Movie.objects.filter(draft=False)
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = MovieFilter


class MovieDetailView(APIView):
    """Вывод фильма"""

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
