# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-10 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20171110_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='image_url',
            field=models.TextField(null=True),
        ),
    ]
