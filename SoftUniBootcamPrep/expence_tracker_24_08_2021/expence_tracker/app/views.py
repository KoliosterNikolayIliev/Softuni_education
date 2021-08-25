from django.shortcuts import render, redirect
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.views.generic.edit import ModelFormMixin
from django.views.generic.list import MultipleObjectMixin

from app.forms import DeleteRecipeForm, ProfileEditForm
from app.models import Profile, Expense


def home(request):
    profile = Profile.objects.exists()
    if profile:
        return HomeView.as_view()(request)
    return AddProfile.as_view()(request)


class HomeView(ListView, MultipleObjectMixin):
    template_name = 'home-with-profile.html'
    model = Expense

    def get(self, request, *args, **kwargs):
        super(HomeView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        context['budget'] = Profile.objects.first().budget
        context['result'] = context['budget'] - sum((x.price for x in context['expense_list']))
        return self.render_to_response(context)


class AddProfile(CreateView):
    model = Profile
    template_name = 'home-no-profile.html'
    fields = '__all__'
    success_url = '/'


class CreateExpenseView(CreateView):
    model = Expense
    template_name = 'expense-create.html'
    fields = '__all__'
    success_url = '/'


class EditExpenseView(UpdateView):
    model = Expense
    template_name = 'expense-edit.html'
    fields = '__all__'
    success_url = '/'


class DeleteExpenseView(DeleteView, ModelFormMixin, DeleteRecipeForm):
    model = Expense
    template_name = 'expense-delete.html'
    success_url = '/'
    form_class = DeleteRecipeForm


def profile(request):
    profile_to_show = Profile.objects.first()
    expenses = profile_to_show.expense_set.all()
    budget_left = profile_to_show.budget - sum((x.price for x in expenses))
    context = {
        'profile': profile_to_show,
        'budget_left': budget_left
    }
    return render(request, 'profile.html', context)


def profile_edit(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = ProfileEditForm(instance=profile)
    context = {'form': form, 'profile': profile}
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile_to_show = Profile.objects.first()
    if request.method == 'POST':
        profile_to_show.delete()
        return redirect('/')
    return render(request, 'profile-delete.html')
