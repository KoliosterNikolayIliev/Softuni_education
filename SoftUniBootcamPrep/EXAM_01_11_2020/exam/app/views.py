from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import ModelFormMixin

from app.forms import DeleteRecipeForm
from app.models import Recipe


class IndexView(ListView):
    template_name = 'index.html'
    model = Recipe


class DetailsView(DetailView):
    template_name = 'details.html'
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super(DetailsView, self).get_context_data(**kwargs)
        ingredients = context.get('object').ingredients.split(', ')
        context['object'].ingredients = ingredients
        return context


class CreateRecipeView(CreateView):
    model = Recipe
    template_name = 'create.html'
    fields = '__all__'
    success_url = '/'


class EditView(UpdateView):
    model = Recipe
    template_name = 'edit.html'
    fields = ['title', 'image_url', 'description', 'ingredients', 'time']
    success_url = '/'


class DeleteRecipeView(DeleteView, ModelFormMixin):
    model = Recipe
    template_name = 'delete.html'
    success_url = '/'
    fields = '__all__'
    # form_class = DeleteRecipeForm
