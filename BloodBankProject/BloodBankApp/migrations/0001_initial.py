
# Generated by Django 3.2.13 on 2022-05-10 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('phno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=250)),
                ('sub', models.CharField(max_length=250)),
                ('bloodgrp', models.CharField(max_length=250)),
            ],
        ),
    ]
