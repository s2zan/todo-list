"""summercoding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import todo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo.views.home, name='home'),
    path('new/', todo.views.new, name='new'),
    path('detail/<int:todo_id>', todo.views.detail, name="detail"),
    path('add/', todo.views.add, name="add"),
    path('update/<int:todo_id>', todo.views.update, name="update"),
    path('complete/', todo.views.complete, name="complete"),
    path('delete/', todo.views.delete, name="delete"),
    path('expired/', todo.views.expired, name="expired"),
    path('priority/<int:priority>', todo.views.priority_view, name="priority"),
]
