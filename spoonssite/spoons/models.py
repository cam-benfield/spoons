from django.db import models
from django.contrib.auth.models import User

class SpoonProfile(models.Model):
    GENDER_CHOICES = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Other', 'Other'),
    )
    COUNT_CHOICES = (
        ('Up', 'Count Up'),
        ('Down', 'Count Down'),
    )
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    user_key = models.AutoField(primary_key=True)
    user_name_string = str(User.username)
    user_gender = models.CharField(max_length=20,
        choices=GENDER_CHOICES,
        default = 'Unknown'
    )
    join_date = models.DateField(auto_now_add=True)
    birthdate = models.DateField('Birthdate')
    average_spoons = models.PositiveIntegerField(default=20)
    count_style = models.CharField(max_length=4,
        choices = COUNT_CHOICES,
        default = 'up'
    )

    def __str__(self):
        return('%s' % self.username)


class SpoonTask(models.Model):
    task_key = models.AutoField(primary_key=True)
    task_user = models.ForeignKey('auth.User')
    task = models.CharField(max_length=20,
    )
    value = models.PositiveIntegerField()

    def __str__(self):
        return str(self.task_user) + '-' + self.task
