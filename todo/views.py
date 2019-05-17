from django.shortcuts import render, get_object_or_404, redirect
from todo.models import Todo

import datetime


def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos, 'noti': notification()})


def detail(request, todo_id):
    todo_detail = get_object_or_404(Todo, id=todo_id)
    return render(request, 'detail.html', {'todo': todo_detail, 'noti': notification()})


def new(request):
    # 새 todo 등록 페이지
    return render(request, 'new.html', {'noti': notification()})


def add(request):
    # db에 넣기
    todo = Todo()
    todo.title = request.GET['title']
    todo.content = request.GET['content']
    todo.priority = request.GET['priority']

    date = request.GET['datepicker'].strip()
    time = time_format(request.GET['timepicker'].strip())

    date = date.replace('.', '-')
    if date == "" :
        date = datetime.today().strftime("%Y-%m-%d")

    todo.deadline = date+" "+time

    print(todo.deadline)
    # 내용 더 들어가야함!!!!!!!!!!!!!!!!!!
    todo.save()

    return redirect('/detail/' + str(todo.id))


def time_format(org):
    if org != "":
        split = org.split()
        head = split[0]
        time = list(map(int, split[1].split(':')))

        if head=='오후':
            time[0] += 12

        org = str(time[0]) + ':' + str(time[1]) + ":00"

    else:
        org = "23:59:59"

    return org


def update(request):
    pass
    #수정 : 수정화면 + 체크박스 바로바로 반영?


def delete(request):
    pass
    # 삭제


def notification():
    # 날짜 지난거 뱃지로 표시하자 (몇개인지...)
    return Todo.objects.filter().count()


def out_of_date(request):
    # expired tasks, unfinished
    # 완수하지 못한 목록만 띄우는 페이지 만들...어..야..하나..?
    todos = Todo.objects.filter()
    return render(request, 'home.html', {'todos': todos})
