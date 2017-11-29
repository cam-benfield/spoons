from django.db import models

class SpoonUser(models.Model):
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


class SpoonTask(models.Model):
    TASK_CHOICES = (
        ('Shower', 'Shower'),
        ('Brush Teeth', 'Brush Teeth'),
        ('Do Homework', 'Do Homework'),
        ('Brush Hair', 'Brush Hair'),
        ('Get Dressed', 'Get Dressed'),
    )

    task_key = models.AutoField(primary_key=True)
    task_user = models.ForeignKey('auth.User')
    task = models.CharField(max_length=20,
        choices=TASK_CHOICES,
        default = 'None'
    )
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.task
