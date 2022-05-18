from rest_framework import serializers

from .models import Movie


class MovieListSerializer(serializers.ModelSerializer):
    """Список фильмов"""

    class Meta:
        model = Movie
        fields = ("id", "title", "videoid", "sub_en", "sub_ru", "url",)


class MovieDetailSerializer(serializers.ModelSerializer):
    """Полный фильм"""

    class Meta:
        model = Movie
        exclude = ("draft", )
