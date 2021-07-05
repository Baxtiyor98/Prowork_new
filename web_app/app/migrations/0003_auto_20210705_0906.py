# Generated by Django 3.2.4 on 2021-07-05 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prog_level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=13, null=True)),
                ('project', models.FileField(upload_to='')),
                ('comment', models.TextField(max_length=2000, null=True)),
                ('level', models.CharField(choices=[('startapp', 'Startupper'), ('worker', 'Practical worker'), ('dev', 'Developer')], max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Developers',
        ),
        migrations.DeleteModel(
            name='Practical_worker',
        ),
        migrations.DeleteModel(
            name='Startapp',
        ),
        migrations.RemoveField(
            model_name='user_details',
            name='level',
        ),
    ]
