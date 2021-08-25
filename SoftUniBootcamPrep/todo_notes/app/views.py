from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import ModelFormMixin

from app.forms import DeleteRecipeForm
from app.models import Note, Profile


def home(request):
    profile = Profile.objects.exists()
    if profile:
        return HomeView.as_view()(request)
    return AddProfile.as_view()(request)


class HomeView(ListView):
    template_name = 'home-with-profile.html'
    model = Note


class AddProfile(CreateView):
    model = Profile
    template_name = 'home-no-profile.html'
    fields = '__all__'
    success_url = '/'


class AddNoteView(CreateView):
    model = Note
    template_name = 'note-create.html'
    fields = '__all__'
    success_url = '/'


class EditNoteView(UpdateView):
    model = Note
    template_name = 'note-edit.html'
    fields = '__all__'
    success_url = '/'


class DeleteNoteView(DeleteView, ModelFormMixin, DeleteRecipeForm):
    model = Note
    template_name = 'note-delete.html'
    success_url = '/'
    # fields = '__all__'
    form_class = DeleteRecipeForm


class DetailsView(DetailView):
    template_name = 'note-details.html'
    model = Note


def profile(request):
    profile_to_show = Profile.objects.first()
    notes = profile_to_show.note_set.count()
    context = {
        'profile': profile_to_show,
        'notes': notes
    }
    if request.method == 'POST':
        profile_to_show.delete()
        return redirect('/')
    return render(request, 'profile.html', context)
