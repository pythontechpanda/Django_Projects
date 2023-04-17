# Generated by Django 4.1.4 on 2023-01-18 07:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Supplier', '0028_alter_commentforpost_date_alter_createpost_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentforpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 18, 13, 4, 12, 385375)),
        ),
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 18, 13, 4, 12, 381378)),
        ),
        migrations.RemoveField(
            model_name='followerscount',
            name='following',
        ),
        migrations.RemoveField(
            model_name='followerscount',
            name='user',
        ),
        migrations.AddField(
            model_name='followerscount',
            name='following',
            field=models.ManyToManyField(blank=True, default=None, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followerscount',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
