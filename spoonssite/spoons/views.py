from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import SpoonTask, SpoonUser

def index(request):
    return render(request, 'spoons/index.html')

def task_list(request):
    tasks = SpoonTask.objects.all() # NOTE: Make User Dynamic
    return render(request, 'spoons/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = SpoonTask.objects.get(pk=pk)
    return render(request, 'spoons/task_detail.html', {'task': task})

def user_list(request):
    users = SpoonUser.objects.all() # NOTE: Make User more Dynamic
    return render(request, 'spoons/user_list.html', {'users': users})

def user_detail(request, pk):
    user = SpoonUser.objects.get(pk=pk)
    return render(request, 'spoons/user_detail.html', {'user': user})
