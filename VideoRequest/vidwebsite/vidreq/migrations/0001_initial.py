# Generated by Django 3.0.4 on 2020-03-31 15:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=20)),
                ('video_desc', models.TextField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2020, 3, 31, 15, 27, 44, 517152, tzinfo=utc))),
            ],
        ),
    ]
