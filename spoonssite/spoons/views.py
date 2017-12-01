from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import SpoonTask, SpoonProfile
from .forms import TaskForm, ProfileForm, UserForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'spoons/index.html')

def login(request):
    return render(request, 'registration/login.html', )

# Task Views
def task_list(request):
    tasks = SpoonTask.objects.all() # NOTE: Make User Dynamic
    return render(request, 'spoons/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = SpoonTask.objects.get(pk=pk)
    return render(request, 'spoons/task_detail.html', {'task': task})

@login_required
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

def task_query(request, pk):
    userobj = SpoonProfile.objects.filter(user_key=pk)
    for item in userobj:
        tasks = SpoonTask.objects.filter(task_user=item.username)
    return render(request, 'spoons/task_query.html', {'tasks': tasks})

# User Views
def user_list(request):
    users = SpoonProfile.objects.all() # NOTE: Make User more Dynamic
    return render(request, 'spoons/user_list.html', {'users': users})

def user_detail(request, pk):
    user = SpoonProfile.objects.get(user_key=pk)
    return render(request, 'spoons/user_detail.html', {'user': user})

@login_required
def user_new(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            usersv = user_form.save(commit=False)
            profilesv = profile_form.save(commit=False)
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile has been added.'))
            return redirect('user_detail', pk=profilesv.user_key)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'spoons/user_new.html', {
        'user_form': user_form,
        'profile_form' : profile_form})
