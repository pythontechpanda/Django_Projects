# Generated by Django 4.1.4 on 2023-01-19 12:13

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Supplier', '0035_createpost_followers_follow_value_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='follow',
            name='post',
            field=models.ManyToManyField(null=True, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='commentforpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 19, 17, 43, 26, 456539)),
        ),
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 19, 17, 43, 26, 437556)),
        ),
        migrations.RemoveField(
            model_name='follow',
            name='following',
        ),
    ]
