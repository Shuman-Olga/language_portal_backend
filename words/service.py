from .models import TopicWord, Word
from django_filters import rest_framework as filters


class WordFilter(filters.FilterSet):
    word = filters.CharFilter(
        field_name='word', lookup_expr='icontains')
    translation = filters.CharFilter(
        field_name='translation', lookup_expr='icontains')
    topic = filters.ModelChoiceFilter(
        queryset=TopicWord.objects.all()
    )

    class Meta:
        model = Word
        fields = ['topic', 'word', ]
