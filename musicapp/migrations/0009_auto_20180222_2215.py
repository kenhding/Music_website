# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-22 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0008_auto_20180221_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='ReleasedDate',
            field=models.DateField(default=None),
        ),
    ]
