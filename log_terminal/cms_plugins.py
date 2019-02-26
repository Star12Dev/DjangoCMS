import os
from os.path import isfile, getsize
import json

from django.contrib.admin.views.main import ChangeList
from django.conf.urls import url
from django.http import HttpResponse, Http404

from log_terminal import app_settings
from django.template.response import TemplateResponse

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from log_terminal.models import *
from django.db import transaction

# loggin Details#
import logging

# Start Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('log_terminal.log')
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)



class ShowLog(CMSPluginBase):
    name = "Show Logs"
    model = LogTerminal #delete this for no modifications
    render_template = "log_terminal/display_log.html"

    def render(self, context, instance, placeholder):
        get_author = context['object'].author

        get_dashboard = context['dashboard']

        file_name = 'resources/user_logs/' + str(get_author).replace(" ", "") + get_dashboard.slug + str(
            get_dashboard.id) + ".log"

        context = super(ShowLog, self).render(context, instance, placeholder)

        with open(file_name , 'r') as f:
            lines = f.read().splitlines()
            if len(lines) > 0:
                last_line = lines[-1]
                logfile = last_line
            else:
                logfile = 'No logs found!'

        position = PluginPosition.objects.filter(model=instance).first()
        logger.debug(position)

        context.update({
            'logfile': logfile,
            'dashboard': str(get_dashboard.slug) + str(get_dashboard.id),
            'author': str(get_author).replace(" ", ""),
            'position':position,
        })
        transaction.commit()

        return context


plugin_pool.register_plugin(ShowLog)
