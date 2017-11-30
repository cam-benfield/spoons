from django import forms
from .models import SpoonTask, SpoonProfile
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):

    class Meta:
        model = SpoonTask
        fields = ('task', 'task_user', 'value',)

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password',)

class ProfileForm(forms.ModelForm):

    class Meta:
        model = SpoonProfile
        fields = ('user_gender', 'birthdate', 'average_spoons', 'count_style',)
