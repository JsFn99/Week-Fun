# Generated by Django 4.2 on 2023-05-06 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Date',
            field=models.DateField(default=18.73148148148148),
        ),
    ]
