# Generated by Django 4.0.3 on 2022-03-03 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_teacher_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
