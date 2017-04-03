from django import forms


class CreateMapForm(forms.Form):
    name = forms.CharField(label='map-name', max_length=100)
    description = forms.CharField(widget=forms.Textarea)



