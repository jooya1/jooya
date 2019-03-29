# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-14 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0002_things_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='things',
            name='title',
            field=models.CharField(default='title', max_length=1000),
        ),
        migrations.AlterField(
            model_name='things',
            name='date_added',
            field=models.DateField(),
        ),
    ]
