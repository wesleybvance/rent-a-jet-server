# Generated by Django 4.1.3 on 2023-08-03 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentajetapi', '0002_flightbooking_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightbooking',
            name='price',
        ),
    ]
