# Generated by Django 4.2 on 2023-05-06 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_event_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Date',
            field=models.DateField(default='10/09/2023'),
            preserve_default=False,
        ),
    ]
