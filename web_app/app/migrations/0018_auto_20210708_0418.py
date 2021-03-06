# Generated by Django 3.2.4 on 2021-07-07 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_startapper_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_type',
        ),
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(default='No bio...'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='avatar',
            field=models.ImageField(blank=True, default="static 'avatar.png'", null=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='comment',
            field=models.TextField(blank=True, default='No comment...', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='user_type',
            field=models.CharField(choices=[('startap', 'Startupper'), ('practice', 'Practitioner'), ('developer', 'Developer')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='avatar',
            field=models.ImageField(blank=True, default="static 'avatar.png'", null=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='comment',
            field=models.TextField(blank=True, default='No comment...', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='programming_language',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='project',
            field=models.FileField(blank=True, null=True, upload_to='project'),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='user_type',
            field=models.CharField(choices=[('startap', 'Startupper'), ('practice', 'Practitioner'), ('developer', 'Developer')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='startapper',
            name='avatar',
            field=models.ImageField(blank=True, default="static 'avatar.png'", null=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='startapper',
            name='comment',
            field=models.TextField(blank=True, default='No comment...', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='startapper',
            name='number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='startapper',
            name='project',
            field=models.FileField(blank=True, null=True, upload_to='project'),
        ),
    ]
