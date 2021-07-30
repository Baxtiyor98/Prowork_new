# Generated by Django 3.2.4 on 2021-07-07 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210707_0506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='practitioner',
            name='skills',
        ),
        migrations.AddField(
            model_name='developer',
            name='user_type',
            field=models.CharField(choices=[('startap', 'Startupper'), ('practice', 'Practitioner'), ('developer', 'Developer')], default='developer', max_length=20),
        ),
        migrations.AddField(
            model_name='practitioner',
            name='user_type',
            field=models.CharField(choices=[('startap', 'Startupper'), ('practice', 'Practitioner'), ('developer', 'Developer')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='developer',
            name='programming_language',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='programming_language',
            field=models.CharField(max_length=200),
        ),
    ]
