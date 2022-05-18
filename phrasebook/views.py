from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .service import PhraseFilter
from .serializers import PhraseListSerializer, TopicPhraseListSerializer
from .models import Phrase, TopicPhrase


class TopicPhraseListView(generics.ListAPIView):
    '''Вывод списка тематик'''
    queryset = TopicPhrase.objects.all()
    serializer_class = TopicPhraseListSerializer


class PhraseListView(generics.ListAPIView):
    '''Вывод списка фраз'''
    queryset = Phrase.objects.filter(draft=False)
    serializer_class = PhraseListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PhraseFilter
