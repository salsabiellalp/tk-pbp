# Generated by Django 4.1.2 on 2022-10-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0005_rename_username_achiever_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='nama',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
