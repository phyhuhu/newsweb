# Generated by Django 3.1.1 on 2020-09-29 03:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspapers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 3, 30, 59, 313626)),
        ),
    ]
