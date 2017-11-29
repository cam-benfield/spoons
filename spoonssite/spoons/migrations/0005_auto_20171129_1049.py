# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 15:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spoons', '0004_user_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpoonTask',
            fields=[
                ('task_key', models.AutoField(primary_key=True, serialize=False)),
                ('task', models.CharField(choices=[('Shower', 'Shower'), ('Brush Teeth', 'Brush Teeth'), ('Do Homework', 'Do Homework'), ('Brush Hair', 'Brush Hair'), ('Get Dressed', 'Get Dressed')], default='None', max_length=20)),
                ('value', models.PositiveIntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='SpoonUser',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_user',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='spoontask',
            name='task_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
