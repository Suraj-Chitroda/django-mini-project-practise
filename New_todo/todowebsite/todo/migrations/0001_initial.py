# Generated by Django 2.2.10 on 2020-05-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todoname', models.CharField(max_length=30)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
