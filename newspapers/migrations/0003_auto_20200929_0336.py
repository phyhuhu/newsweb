# Generated by Django 3.1.1 on 2020-09-29 03:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newspapers', '0002_auto_20200929_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
