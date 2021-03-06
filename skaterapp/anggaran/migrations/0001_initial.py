# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kegiatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kegiatan', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_program', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='kegiatan',
            name='nama_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anggaran.Program'),
        ),
    ]
