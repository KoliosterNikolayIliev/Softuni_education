from django.shortcuts import render


def index(request):
    return render(request, 'second__app/index.html')
