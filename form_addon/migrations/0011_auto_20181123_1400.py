# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-23 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form_addon', '0010_auto_20181123_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formbtnpluginposition',
            name='model',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='btn_position', to='form_addon.FormPlugin'),
        ),
    ]
