# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-08 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blero_grid', '0002_gridcells_cell_font_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gridcells',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cells', to='blero_grid.BleroGrid'),
        ),
        migrations.AlterField(
            model_name='gridcolumns',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='blero_grid.BleroGrid'),
        ),
        migrations.AlterField(
            model_name='gridrows',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='blero_grid.BleroGrid'),
        ),
    ]