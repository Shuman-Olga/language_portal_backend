from rest_framework import serializers

from .models import TopicWord, Word


class TopicWordListSerializer(serializers.ModelSerializer):
    '''Список тематик '''
    class Meta:
        model = TopicWord
        fields = '__all__'


class WordListSerializer(serializers.ModelSerializer):
    '''Список слов'''
    class Meta:
        model = Word
        fields = '__all__'


class WordDetailSerializer(serializers.ModelSerializer):
    '''Слово'''
    topic = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Word
        exclude = ("draft",)
