from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .service import WordFilter
from rest_framework import filters
from .models import TopicWord, Word
from .serializers import TopicWordListSerializer, WordListSerializer
from django.db.models.functions import Lower


class TopicWordListView(generics.ListAPIView):
    '''Вывод списка тематик'''
    queryset = TopicWord.objects.all()
    serializer_class = TopicWordListSerializer


class WordListView(generics.ListAPIView):
    '''Вывод списка слов'''
    queryset = Word.objects.filter(
        draft=False)
    serializer_class = WordListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = WordFilter

    # def get_queryset(self):
    #     return Word.objects.order_by().values('word').distinct(

# class WordDetailView(generics.ListAPIView):
#     """Вывод слова"""

#     queryset = Word.objects.get(draft=False)
#     serializer_class = WordDetailSerializer()
