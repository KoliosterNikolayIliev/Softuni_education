from django import forms

from app.models import Profile, Expense


class ProfileCreate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['budget', 'first_name', 'last_name']


class ExpenseCreate(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'description', 'link_to_image', 'price', 'profile']


class DisabledFormMixin():
    def __init__(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True


class DeleteExpenseForm(ExpenseCreate, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
