from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone

from todo.models import Todo

import json


def home(request):
    todos = Todo.objects.all().order_by('-updated_at')
    today = timezone.datetime.today().date()
    return render(request, 'home.html', {'title':"전체", 'todos': todos, 'noti': notification(), 'today': today, 'noti_un':noti_uncompleted()})


def detail(request, todo_id):
    todo_detail = get_object_or_404(Todo, id=todo_id)
    return render(request, 'detail.html', {'todo': todo_detail, 'noti': notification(), 'noti_un':noti_uncompleted()})


def new(request):
    return render(request, 'new.html', {'noti': notification(), 'noti_un':noti_uncompleted()})


def add(request):
    # db에 넣기
    todo = Todo()
    todo.title = request.GET['title']
    todo.content = request.GET['content']
    todo.priority = request.GET['priority']

    date = request.GET['datepicker'].strip()
    time = request.GET['timepicker'].strip()

    if date != "" or time != "":
        time = time_format(time)
        date = date.replace('.', '-')
        if date == "":
            date = timezone.datetime.today().strftime("%Y-%m-%d")

        todo.deadline = date+" "+time

    todo.updated_at = timezone.datetime.today()
    todo.save()

    return redirect('/')


def time_format(org):
    if org != "":
        split = org.split()
        head = split[0]
        time = list(map(int, split[1].split(':')))
        if head == '오후':
            time[0] += 12

        org = str(time[0]) + ':' + str(time[1]) + ":00"

    else:
        org = "23:59:59"
    return org


def update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.title = request.GET['title']
    todo.content = request.GET['content']
    todo.priority = request.GET['priority']

    date = request.GET['datepicker'].strip()
    time = request.GET['timepicker'].strip()

    if date != "" or time != "":
        time = time_format(time)
        date = date.replace('.', '-')
        if date == "":
            date = timezone.datetime.today().strftime("%Y-%m-%d")

        todo.deadline = date+" "+time
    else:
        todo.deadline = None

    todo.updated_at = timezone.datetime.today()

    todo.save()

    return redirect('/')


def complete(request):
    todo_id = request.POST.get('todo_id', None)
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed

    context = {'status': todo.completed}
    todo.save()

    return HttpResponse(json.dumps(context), content_type="application/json")


def delete(request):
    todo_id = request.POST.get('todo_id', None)
    todo = get_object_or_404(Todo, id=todo_id)
    print(todo)
    todo.delete()
    print(todo)

    context = {'result': 'deleted'}
    return HttpResponse(json.dumps(context), content_type="application/json")


def notification():
    return Todo.objects.filter(completed=False, deadline__isnull=False, deadline__lt=timezone.datetime.now()).count()


def noti_uncompleted():
    return Todo.objects.filter(completed=False).count()


def expired(request):
    todos = Todo.objects.filter(completed=False, deadline__isnull=False, deadline__lt=timezone.datetime.now()).order_by('-deadline')
    date = {}
    for todo in todos:
        deadline = str(todo.deadline.date())
        if deadline not in date:
            date[deadline] = []
        date[deadline].append(todo)

    return render(request, 'expired.html', {'date': date, 'noti': notification(), 'title': "기한 만료", 'noti_un':noti_uncompleted()})


def uncompleted(request):
    todos = Todo.objects.filter(completed=False).order_by('deadline')
    date = {}
    nodeadline = []

    for todo in todos:
        if todo.deadline == None:
            nodeadline.append(todo)
            continue

        deadline = str(todo.deadline.date())
        if deadline not in date:
            date[deadline] = []
        date[deadline].append(todo)

    today = timezone.datetime.today().date()
    return render(request, 'expired.html', {'nodeadline': nodeadline, 'date': date, 'noti': notification(), 'title': '미완료', 'today':today, 'noti_un':noti_uncompleted()})


def priority_view(request, priority):
    todos = Todo.objects.filter(priority=priority).order_by('-updated_at')
    if priority==2:
        title = "매우 중요"
    elif priority==1:
        title = "중요"
    else:
        title = "보통"

    today = timezone.datetime.today().date()
    return render(request, 'home.html', {'title': title, 'todos': todos, 'noti': notification(), 'today': today, 'noti_un':noti_uncompleted()})