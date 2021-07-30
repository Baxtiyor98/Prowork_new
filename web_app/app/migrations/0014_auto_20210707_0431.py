# Generated by Django 3.2.4 on 2021-07-06 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0013_customuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='startapper',
            name='number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='startapper',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='IdeaStartapper',
        ),
    ]
