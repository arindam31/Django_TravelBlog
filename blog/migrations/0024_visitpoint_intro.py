# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_visitpoint_must_see'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitpoint',
            name='intro',
            field=models.CharField(blank=True, default=b'', max_length=200),
        ),
    ]
