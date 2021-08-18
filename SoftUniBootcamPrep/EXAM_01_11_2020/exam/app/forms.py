from django import forms

from app.models import Recipe


class DeleteRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image_url', 'description', 'ingredients', 'time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True


