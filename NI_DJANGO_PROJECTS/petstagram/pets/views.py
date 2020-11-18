from django.shortcuts import render, redirect

# Create your views here.
from pets.models import Pet, Like


def pet_details(request,pk):
    # here we take the the pk from pets.urls (<int:pk>)
    # context is the objects that we return to the site
    context = {'pet': Pet.objects.get(pk=pk)}
    return render(request, 'pets/pet_detail.html', context)


def pet_list(request):
    context = {'pets': Pet.objects.all(), }
    return render(request, 'pets/pet_list.html', context)


def like_pet(request,pk):
    pet = Pet.objects.get(pk=pk)
    pet.add(Like())
    pet.save()
    return redirect('')
