# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-18 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('pw', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=10)),
                ('expert', models.BooleanField(default=False)),
            ],
        ),
    ]
