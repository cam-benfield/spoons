from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import SpoonTask, SpoonUser
from .forms import TaskForm, UserForm

def index(request):
    return render(request, 'spoons/index.html')

# Task Views
def task_list(request):
    tasks = SpoonTask.objects.all() # NOTE: Make User Dynamic
    return render(request, 'spoons/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = SpoonTask.objects.get(pk=pk)
    return render(request, 'spoons/task_detail.html', {'task': task})

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_detail', pk=task.task_key)
    else:
        form = TaskForm()
    return render(request, 'spoons/task_new.html', {'form': form})

def task_query(request, user):
    us = str(auth.User)
    tasks = SpoonTask.objects.get(task_user=us)
    return render(request, 'task_query.html', {'tasks': tasks})

# User Views
def user_list(request):
    users = SpoonUser.objects.all() # NOTE: Make User more Dynamic
    return render(request, 'spoons/user_list.html', {'users': users})

def user_detail(request, pk):
    user = SpoonUser.objects.get(pk=pk)
    return render(request, 'spoons/user_detail.html', {'user': user})

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_detail', pk=user.user_key)
    else:
        form = UserForm()
    return render(request, 'spoons/user_new.html', {'form': form})

def user_query(request, tk): # finds users who have the task
    users = SpoonTask.objects.filter(tk)
    return render(request, '/user_query.html', {'users': users})
