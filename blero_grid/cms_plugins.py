# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.forms.models import model_to_dict

from blero_grid.models import *
from . import models
import json


import os




# loggin Details#
import logging
#Start Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('blero_grid.log')
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))






class BleroGridPlugin(CMSPluginBase):
    model = BleroGrid
    name = 'Blero Grid'
    render_template = "blero_grid/grid_base.html"


    def render(self, context, instance, placeholder):

        data=[]

        active_grid = BleroGrid.objects.get(pk=instance.pk)
        grid_values=GridCells.objects.all().filter(model=active_grid)

        cell_data={}
        for cell in grid_values:
            cell_data[cell.row_number]={'column_number':cell.column_number,'cell_content':cell.cell_content}



        columns = int(instance.grid_columns)
        rows=int(instance.grid_rows)


        position = PluginPosition.objects.filter(model=instance).first()
        context.update({
            'instance': instance,
            'cell_data': cell_data,
            'position': position,
            'columns': [i for i in range(columns)],
            'rows': [i for i in range(rows)],
        })

        return context





plugin_pool.register_plugin(BleroGridPlugin)
