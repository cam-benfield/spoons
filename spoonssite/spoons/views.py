from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Task, User

def index(request):
    return render(request, 'spoons/index.html')

def task_list(request):
    tasks = Task.objects() # NOTE: Make User Dynamic
    return render(request, 'spoons/task_list.html', {'tasks': tasks})

def user_list(request):
    return render(request, 'spoons/user_list.html')
