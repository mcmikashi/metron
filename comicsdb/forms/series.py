from django.forms import (ModelForm, TextInput, Textarea, Select)

from comicsdb.models import Series


class SeriesForm(ModelForm):

    class Meta:
        model = Series
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'input'}),
            'slug': TextInput(attrs={'class': 'input'}),
            'sort_name': TextInput(attrs={'class': 'input'}),
            'volume': TextInput(attrs={'class': 'input'}),
            'year_began': TextInput(attrs={'class': 'input'}),
            'year_end': TextInput(attrs={'class': 'input'}),
            'series_type': Select(attrs={'class': 'input'}),
            'publisher': Select(attrs={'class': 'select'}),
            'short_desc': TextInput(attrs={'class': 'input'}),
            'desc': Textarea(attrs={'class': 'textarea'}),
        }
