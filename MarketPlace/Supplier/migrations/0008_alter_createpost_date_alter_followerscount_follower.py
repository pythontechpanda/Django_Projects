# Generated by Django 4.1.4 on 2023-01-14 06:35

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Supplier', '0007_alter_createpost_date_remove_followerscount_follower_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 14, 12, 5, 18, 299634)),
        ),
        migrations.AlterField(
            model_name='followerscount',
            name='follower',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
