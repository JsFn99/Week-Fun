# Generated by Django 4.2 on 2023-05-06 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='Date',
        ),
    ]
