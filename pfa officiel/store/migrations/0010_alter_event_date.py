# Generated by Django 4.2 on 2023-05-06 03:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 1, 1)),
        ),
    ]
