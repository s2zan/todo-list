from django.shortcuts import render
from todo.models import Todo

def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})