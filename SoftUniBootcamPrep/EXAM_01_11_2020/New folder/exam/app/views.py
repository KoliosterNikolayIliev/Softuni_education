from django.shortcuts import render, redirect

from app.forms import RecipeForm, DeleteRecipeForm
from app.models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'index.html', context)


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = list(recipe.ingredients.split(', '))
    context = {'recipe': recipe, 'ingredients':ingredients}
    return render(request, 'details.html', context)


def create(request):
    if request.method == 'GET':
        form = RecipeForm()
        context = {'form': form, }
        return render(request, 'create.html', context)
    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {'form': form, }
        return render(request, 'create.html', context)


def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
        context = {'form': form, 'recipe': recipe}
        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {'form': form, 'recipe': recipe}
        return render(request, 'edit.html', context)


def delete(request,pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteRecipeForm(instance=recipe)
        context = {'form': form, 'recipe': recipe}
        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('index')
