
# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.forms.models import model_to_dict

from datetime import datetime
from task_tracker.models import *
from . import models
import json

import os


# loggin Details#
import logging

# Start Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('task_tracker.log')
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)



class TaskHolderPlugin(CMSPluginBase):
    model = TaskHolder
    name = 'Task Tracker'
    render_template = "task_tracker/tt_base.html"


    def render(self, context, instance, placeholder):


        active_task_holder = TaskHolder.objects.get(pk=instance.pk)
        tasks=TaskDetail.objects.all().filter(model=active_task_holder)
        task_details={}

        for task in tasks:
            if task.is_complete == False:
                days_outstanding = (datetime.now().date() - task.date_created).days
                task_details[task.pk] = {'title': task.task_title, 'task_body': task.task_body,
                                         'is_complete': task.is_complete, 'days_left': days_outstanding}

        if active_task_holder.only_completed == False:

            for task in tasks:
                if task.is_complete == True:
                    days_outstanding = 0
                    task_details[task.pk] = {'title': task.task_title, 'task_body': task.task_body,
                                             'is_complete': task.is_complete, 'days_left': days_outstanding}

        logger.debug(task_details)

        only_completed=instance.only_completed

        position = PluginPosition.objects.filter(model=instance).first()
        context.update({
            'instance': instance,
            'only_completed': only_completed,
            'tasks':task_details,
            'position':position,

        })

        return context





plugin_pool.register_plugin(TaskHolderPlugin)
