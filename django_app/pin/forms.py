from django import forms


class CreateMap(forms.Form):
    name = forms.CharField(label='map-name', max_length=100)
    description = forms.Textarea()
    is_private = forms.BooleanField()


