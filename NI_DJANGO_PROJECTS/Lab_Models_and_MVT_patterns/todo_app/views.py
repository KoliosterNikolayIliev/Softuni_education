from django.shortcuts import render
from todo_app.models import Todo


# Create your views here.
def index(requirements):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(requirements, 'todo_app/index.html', context=context)


