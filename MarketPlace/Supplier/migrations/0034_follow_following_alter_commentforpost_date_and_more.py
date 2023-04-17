# Generated by Django 4.1.4 on 2023-01-19 09:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Supplier', '0033_follow_delete_followerscount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commentforpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 19, 14, 45, 20, 154390)),
        ),
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 19, 14, 45, 20, 149394)),
        ),
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('user', 'following')},
        ),
        migrations.RemoveField(
            model_name='follow',
            name='followed',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='followed_on',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='updated_on',
        ),
    ]