from django_filters.rest_framework import filters
from django_filters.rest_framework import FilterSet

from reviews.models import Cats, Porode


class CatsFilter(FilterSet):
    """Модель фильтрации по породе котят."""
    porode_cats = filters.ModelChoiceFilter(
        queryset=Porode.objects.all(),
        label='Порода котенка',
        empty_label='Выберите породу'
    )

    class Meta:
        model = Cats
        fields = ['porode_cats']
