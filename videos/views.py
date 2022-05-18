from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from .service import VideoFilter
from .models import TopicVideo, Video
from .serializers import TopicVideoListSerializer, VideoDetailSerializer


class TopicVideoListView(generics.ListAPIView):
    '''Вывод списка тематик'''
    queryset = TopicVideo.objects.all()
    serializer_class = TopicVideoListSerializer


class VideoListView(generics.ListAPIView):
    """Вывод списка фильмов"""
    queryset = Video.objects.filter(draft=False)
    serializer_class = VideoDetailSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = VideoFilter


class VideoDetailView(APIView):
    """Вывод фильма"""

    def get(self, request, pk):
        movie = Video.objects.get(id=pk, draft=False)
        serializer = VideoDetailSerializer(movie)
        return Response(serializer.data)
