from django.shortcuts import render
from todo.models import Todo


def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})


def add(request):
    return render(request, 'add.html')


def deadline(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})


def complete(request, id):
    todo = Todo.objects.get(id=id)
    return

