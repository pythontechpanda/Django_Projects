# Generated by Django 4.1.3 on 2023-03-01 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_getclubbyuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='getclubbyuser',
            old_name='club',
            new_name='clubid',
        ),
        migrations.RenameField(
            model_name='getclubbyuser',
            old_name='clubuser',
            new_name='userid',
        ),
    ]
