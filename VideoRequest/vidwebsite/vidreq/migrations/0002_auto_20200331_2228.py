# Generated by Django 3.0.4 on 2020-03-31 16:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vidreq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
