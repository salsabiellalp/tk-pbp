# Generated by Django 4.1 on 2022-10-29 15:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wastedeposit',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
