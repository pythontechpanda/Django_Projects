# Generated by Django 3.2.4 on 2023-01-30 06:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0038_alter_commentforpost_date_alter_createpost_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentforpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 30, 11, 42, 11, 970280)),
        ),
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 30, 11, 42, 11, 934313)),
        ),
    ]