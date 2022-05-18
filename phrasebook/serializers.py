from rest_framework import serializers

from .models import Phrase, TopicPhrase


class TopicPhraseListSerializer(serializers.ModelSerializer):
    '''Список тематик'''
    class Meta:
        model = TopicPhrase
        fields = '__all__'


class PhraseListSerializer(serializers.ModelSerializer):
    '''Список фраз'''
    class Meta:
        model = Phrase
        fields = ("id", "text", "translation", "topic",)
