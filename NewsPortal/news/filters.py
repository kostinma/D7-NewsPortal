from datetime import datetime

from django.contrib.auth.models import User
from django.forms import DateInput

from django_filters import (
    FilterSet, # Not in Django, python -m pip install django-filter==21.1
    CharFilter,
    DateFilter,
    ModelChoiceFilter,
    ModelMultipleChoiceFilter, # filtering over several things
)

from .models import (
    Post,
    Author,
    # Category,
    # Comment,
)

# Filters for model Post
class SearchPostFilter(FilterSet):    # use it in views.py
    # title = CharFilter(field_name = 'title', label='Header', lookup_expr='icontains')

    # models.py: time_in = models.DateTimeField(auto_now_add=True)
    time_in = DateFilter(
        # field_name='time_in',
        label='Published after',
        lookup_expr='gt',
        widget=DateInput(attrs={'type': 'date'}), # generate form <input type="date">, get input
    )

    author__user = ModelChoiceFilter(
        field_name = 'author__user',
        queryset = User.objects.all(),
        label = 'Author',
        empty_label = 'All',
        # conjoined=True
    )

    # Filters to work with GET queries
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }


# End of file
