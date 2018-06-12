# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20180606_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('street', models.TextField()),
                ('pincode', models.PositiveIntegerField(blank=True)),
                ('timings', models.CharField(blank=True, max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.City')),
                ('city_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.CityPost')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
