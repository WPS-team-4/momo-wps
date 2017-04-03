from django import forms


class CreateMapForm(forms.Form):
    map_name = forms.CharField(label='map-name', max_length=100)
    description = forms.CharField(widget=forms.Textarea)


class CreatePinForm(forms.Form):
    pin_name = forms.CharField(label='pin-name', max_length=100)
