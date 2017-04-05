from django import forms


class MapCreateForm(forms.Form):
    name = forms.CharField(label='map name', max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    # my_map = forms.ModelChoiceField(queryset=Map.objects.filter(author=))


class PinCreateForm(forms.Form):
    name = forms.CharField(label='pin name', max_length=100)
