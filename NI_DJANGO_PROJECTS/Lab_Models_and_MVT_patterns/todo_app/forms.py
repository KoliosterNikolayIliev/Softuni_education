from django import forms

class TodoForm(forms.Form):
    title = forms.CharField(label='title', max_length=20)
    description = forms.CharField(widget=forms.Textarea)




def check_for_name(value):
    if not value[0].isupper():
        raise forms.ValidationError("Name needs to start with an uppercase letter")

def check_for_age(value):
    pass

def check_for_password(value):
    pass

class FormName(forms.Form):
    name = forms.CharField(validators=check_for_name())
