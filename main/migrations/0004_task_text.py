# Generated by Django 4.0.5 on 2022-08-19 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_task_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='text',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
