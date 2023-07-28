# Generated by Django 4.2 on 2023-05-02 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('Adresse', models.CharField(max_length=240)),
                ('Lowest_Price', models.FloatField(default=0.0)),
                ('Highest_Price', models.FloatField(default=0.0)),
                ('Availibility', models.BooleanField(default=True)),
                ('Description', models.TextField(blank=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
