from .models import Phrase
from django_filters import rest_framework as filters


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PhraseFilter(filters.FilterSet):
    topic = CharFilterInFilter(field_name="topic__id", lookup_expr='in')

    class Meta:
        model = Phrase
        fields = ['topic']
