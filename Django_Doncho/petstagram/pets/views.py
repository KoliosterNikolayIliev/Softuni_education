from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from pets.forms import CommentForm, PetForm
from pets.tools.clean_up import clean_up_files

from pets.models import Pet, Like, Comment

def index(request):
    return render(request, 'index.html')

def list_pets(request):
    pets = Pet.objects.filter(type='pic')
    context = {
        'pets': pets,
    }

    return render(request, 'pet_list.html', context)

def list_mods(request):
    mods = Pet.objects.filter(type='mod')
    context = {
        'mods': mods,
    }

    return render(request, 'mod_list.html', context)


def details_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
            'form': CommentForm(),
            'can_delete': request.user == pet.user,
            'can_edit': request.user == pet.user,
            'can_like': request.user != pet.user,
            'can_comment': request.user != pet.user,
            'has_liked': pet.like_set.filter(user_id=request.user.id).exists(),
        }

        return render(request, 'pet_detail.html', context)
    else:
        if pet.user == request.user:
            return HttpResponse('FORBIDDEN !')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.user = request.user
            comment.pet = pet
            comment.save()
            return redirect('pet details or comment', pk)
        context = {
            'pet': pet,
            'form': form,

        }

        return render(request, 'pet_detail.html', context)


def persist_pet(request, pet, template_name):
    if request.method == 'GET':
        user = request.user
        form = PetForm(instance=pet, initial={'user': user})
        form.fields['user'].widget = forms.HiddenInput()

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'{template_name}.html', context)
    else:
        old_image = pet.image
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            likes = Like.objects.filter(pet_id=pet.pk)
            likes.delete()
            if old_image:
                clean_up_files(old_image.path)
            return redirect('pet details or comment', pet.pk)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'{template_name}.html', context)


# @user_required(Pet, methods=['GET'])
def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if pet.user != request.user:
        return HttpResponse('FORBIDDEN !')
    return persist_pet(request, pet, 'pet_edit')


@login_required(redirect_field_name='registration/login.html')
def create_pet(request):
    pet = Pet()
    return persist_pet(request, pet, 'pet_create')


@login_required(redirect_field_name='registration/login.html')
def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if pet.user != request.user:
        return HttpResponse('FORBIDDEN !')
    if request.method == 'GET':
        context = {
            'pet': pet,
        }

        return render(request, 'pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')


@login_required(redirect_field_name='registration/login.html')
def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    likes = pet.like_set.filter(user_id=request.user.id)
    like = Like(test=str(pk))
    if likes.exists():
        likes.delete()
    else:
        like.pet = pet
        like.user = request.user
        like.save()
    return redirect('pet details or comment', pk)


# Long, non-reusable variants of create and edit
def edit_pet_long(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        form = PetForm(instance=pet)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, 'pet_edit.html', context)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details or comment', pet.pk)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'pet_edit.html', context)


def create_pet_long(request):
    if request.method == 'GET':
        form = PetForm()

        context = {
            'form': form,
        }

        return render(request, 'pet_create.html', context)
    else:
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save()
            return redirect('pet details or comment', pet.pk)

        context = {
            'form': form,
        }

        return render(request, f'pet_edit.html', context)
