# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-16 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0005_merge_20190316_0249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='things',
            name='name',
        ),
    ]
