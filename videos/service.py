from .models import TopicVideo, Video
from django_filters import rest_framework as filters


class VideoFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    topic = filters.ModelChoiceFilter(
        queryset=TopicVideo.objects.all()
    )

    class Meta:
        model = Video
        fields = ['topic', 'title']
