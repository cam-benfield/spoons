from django.db import models

class User(models.Model):
    GENDER_CHOICES = (
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
        ('OTHER', 'Other'),
    )

    user_key = models.AutoField(primary_key=True)
    user_name = models.ForeignKey('auth.User')
    user_gender = models.CharField(max_length=20,
        choices=GENDER_CHOICES,
        default = 'UNKNOWN'
    )
    join_date = models.DateTimeField('Date Joined')
    birthdate = models.DateTimeField('Birthdate')
    average_spoons = models.PositiveIntegerField()

    def __str__(self):
        return('%s' % self.user_name)


class Task(models.Model):
    TASK_CHOICES = (
        ('SHOWER', 'Shower'),
        ('BRUSH TEETH', 'Brush Teeth'),
        ('DO HOMEWORK', 'Do Homework'),
        ('BRUSH HAIR', 'Brush Hair'),
        ('GET DRESSED', 'Get Dressed'),
    )

    task_key = models.AutoField(primary_key=True)
    task_user = models.ForeignKey('auth.User')
    task = models.CharField(max_length=20,
        choices=TASK_CHOICES,
        default = 'SHOWER'
    )
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.task
