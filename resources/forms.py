from django import forms

from .models import Resource

# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = [
            'title',
            'link',
            'description',
            'for_total_beginners',
            'tags'
        ]
        labels = {
            'title': 'Tytuł/Nazwa',
            'link': 'Link',
            'description': 'Opis',
            'for_total_beginners': 'Czy jest dobry dla początkujących?',
            'tags': 'Tagi',
        }
        help_texts = {
            'title': 'Oficjalna nazwa materiału',
            'link': 'Wklej dokładnie cały adres',
            'tags': 'Tagi można oddzielać spacjami. Jeśli tag zawiera dwa wyrazy lub więcej to wszystkie tagi muszą zostać oddzielone przecinkami. <br/> Wypisz wszystkie języki programowania/narzędzia, których uczy ten materiał.'
        }

    def __init__(self, *args, **kwargs):
        super(ResourceForm, self).__init__(*args, **kwargs)
        self.fields['for_total_beginners'].required = True
        for f in self.fields.values():
            if not f.required:
                continue
            f.widget.attrs.setdefault('required', True)
            f.label = '{} *'.format(f.label)
