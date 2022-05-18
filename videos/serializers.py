from rest_framework import serializers
from .models import TopicVideo, Video


class TopicVideoListSerializer(serializers.ModelSerializer):
    '''Список тематик '''
    class Meta:
        model = TopicVideo
        fields = '__all__'


class VideoListSerializer(serializers.ModelSerializer):
    """Список фильмов"""

    class Meta:
        model = Video
        fields = ("id", "title", "videoid", "topic", "url",)


class VideoDetailSerializer(serializers.ModelSerializer):
    """Полный фильм"""

    class Meta:
        model = Video
        exclude = ("draft", )
