# Generated by Django 4.1.3 on 2023-03-20 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccounts',
            name='user',
        ),
        migrations.RemoveField(
            model_name='creditcards',
            name='user',
        ),
        migrations.RemoveField(
            model_name='creditline',
            name='user',
        ),
        migrations.RemoveField(
            model_name='demataccounts',
            name='user',
        ),
        migrations.RemoveField(
            model_name='investment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='itrandtax',
            name='user',
        ),
        migrations.RemoveField(
            model_name='personalloan',
            name='user',
        ),
    ]