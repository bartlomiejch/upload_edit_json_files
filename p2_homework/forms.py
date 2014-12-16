from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Wybierz plik',
        help_text='max. 42 MB'
    )