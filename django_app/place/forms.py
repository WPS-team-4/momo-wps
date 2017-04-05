from django import forms


class SearchPlaceForm(forms.Form):
    keyword = forms.CharField(label='search', max_length=100)
