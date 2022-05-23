from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from .service import WordFilter
from rest_framework import filters
from .models import TopicWord, Word
from .serializers import TopicWordListSerializer, WordDetailSerializer, WordListSerializer


class TopicWordListView(generics.ListAPIView):
    '''Вывод списка тематик'''
    queryset = TopicWord.objects.all()
    serializer_class = TopicWordListSerializer


class WordViewSet(viewsets.ReadOnlyModelViewSet):
    '''Вывод списка слов'''
    queryset = Word.objects.all().order_by('word')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = WordFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return WordListSerializer
        elif self.action == "retrieve":
            return WordDetailSerializer

    # def get_queryset(self):
    #     return Word.objects.order_by().values('word').distinct(


# class WordDetailView(generics.RetrieveAPIView):
#     """Вывод слова"""

#     queryset = Word.objects.filter(draft=False)
#     serializer_class = WordDetailSerializer


class WordRandomView(generics.RetrieveAPIView):
    """Вывод рандомного слова"""

    queryset = Word.objects.filter(draft=False)
    serializer_class = WordDetailSerializer
