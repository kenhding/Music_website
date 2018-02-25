# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-20 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0006_auto_20180220_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='NumberAlbum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artist',
            name='PictureURL',
            field=models.URLField(default=''),
        ),
    ]
