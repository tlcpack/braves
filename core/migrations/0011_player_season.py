# Generated by Django 3.0.6 on 2020-07-19 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200718_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='season',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
