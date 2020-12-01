from django import forms
from django.forms import ModelForm

from pets.models import Pet


class PetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        ModelForm.__init__(self, *args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {'image_url': forms.TextInput(attrs={'id': 'img_input', })}


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control rounded-2', }))
