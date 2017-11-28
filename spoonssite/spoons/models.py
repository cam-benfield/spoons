from django.db import models

class User(models.Model):
    user_key = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    join_date = models.DateTimeField('Date Joined')
    birthdate = models.DateTimeField('Birthdate')
    average_spoons = models.PositiveIntegerField()

    def __str__(self):
        return self.user_key

    def create_user(self):
        pass

class Task(models.Model):
    task_key = models.AutoField(primary_key=True)
    task = models.CharField(max_length=60)
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.task_key
