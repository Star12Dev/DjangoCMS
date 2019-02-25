# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


from . import models



import csv
import os


from django.shortcuts import render
from blero_container.models import *




# loggin Details#
import logging
#Start Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('blero_container.log')
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BleroContainerPlugin(CMSPluginBase):
    model = BleroContainer
    name = 'Add Blero Container'
    render_template = "blero_container/base.html"


    def render(self, context, instance, placeholder):

        columns=range(int(instance.number_columns))
        col_width=100/int(instance.number_columns)
        position = PluginPosition.objects.filter(model=instance).first()
        context.update({
            'instance': instance,
            'columns':columns,
            'col_w':col_width,
            'position': position,

        })

        return context





plugin_pool.register_plugin(BleroContainerPlugin)
