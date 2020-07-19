# Generated by Django 3.0.6 on 2020-07-19 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200719_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=6)),
                ('players', models.ManyToManyField(to='core.Player')),
            ],
        ),
    ]
