# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anggaran', '0007_auto_20170817_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usulandanaanggaran',
            name='jumlah_anggaran',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=64),
        ),
    ]