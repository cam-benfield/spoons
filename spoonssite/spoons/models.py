from django.db import models

class User(models.Model):
    user_key = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    join_date = models.DateTimeField('Date Joined')
    birthdate = models.DateTimeField('Birthdate')
    average_spoons = models.PositiveIntegerField()

class Tasks(models.Model):
    user_ref_key = User.user_key
    task = models.CharField(max_length=60)
    value = models.PositiveIntegerField()
