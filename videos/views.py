from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics, viewsets
from .service import VideoFilter
from .models import TopicVideo, Video
from .serializers import TopicVideoListSerializer, VideoDetailSerializer, VideoListSerializer


class TopicVideoListView(generics.ListAPIView):
    '''Вывод списка тематик'''
    queryset = TopicVideo.objects.all()
    serializer_class = TopicVideoListSerializer


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка фильмов"""
    queryset = Video.objects.filter(draft=False)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = VideoFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return VideoListSerializer
        elif self.action == "retrieve":
            return VideoDetailSerializer
