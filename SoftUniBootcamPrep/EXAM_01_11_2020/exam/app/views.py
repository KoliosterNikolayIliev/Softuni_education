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

  #TODO - fix ingredients
# def details(request, pk):
#     recipe = Recipe.objects.get(pk=pk)
#     ingredients = list(recipe.ingredients.split(', '))
#     context = {'recipe': recipe, 'ingredients':ingredients}
#     return render(request, 'details.html', context)


class CreateRecipeView(CreateView):
    model = Recipe
    template_name = 'create.html'
    fields = ['title', 'image_url', 'description', 'ingredients', 'time']
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
    form_class = DeleteRecipeForm
