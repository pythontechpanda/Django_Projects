# Generated by Django 3.2.4 on 2023-01-30 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0043_auto_20230130_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentforpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 30, 17, 46, 44, 966596)),
        ),
        migrations.AlterField(
            model_name='createpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 30, 17, 46, 44, 924634)),
        ),
    ]
