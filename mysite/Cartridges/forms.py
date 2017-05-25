from django import forms

class UrlForm(forms.Form):
    Url = forms.CharField(label='Datasource', max_length=100)
