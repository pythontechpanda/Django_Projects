# Generated by Django 4.1.4 on 2023-01-20 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follower',
            field=models.ManyToManyField(to='accounts.follow'),
        ),
    ]
