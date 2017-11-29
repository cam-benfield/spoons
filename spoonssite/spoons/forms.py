from django import forms
from .models import SpoonTask, SpoonUser

class TaskForm(forms.ModelForm):

    class Meta:
        model = SpoonTask
        fields = ('task', 'task_user', 'value',)

class UserForm(forms.ModelForm):

    class Meta:
        model = SpoonUser
        fields = ('user_name', 'user_gender', 'birthdate', 'average_spoons',)
