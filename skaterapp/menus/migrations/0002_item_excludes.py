# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='excludes',
            field=models.TextField(blank=True, help_text='Separated each item by comma', null=True),
        ),
    ]
