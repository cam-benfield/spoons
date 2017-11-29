from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! You're at the spoons index!")

def task_list(request):
    return render(request, 'spoons/task_list.html')

def user_list(request):
    return render(request, 'spoons/user_list.html')
