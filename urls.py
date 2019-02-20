# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls
from form_addon.views import *
from blero_grid.views import *
from dashboards_app.views import *
from task_tracker.views import  *
from log_terminal.views import log_checker

urlpatterns = [
    # add your own patterns here

    url(r'^form-addon/', form_addon),
    url(r'^blero_grid/', save_grid),
    url(r'^plugin_position/(?P<plugin_type>[\w.-]+)/$', plugin_position),
    url(r'^check-log/$', log_checker),
    url(r'^create_task/',create_task),#task tracker url
    url(r'^delete_task/',delete_task),#task tracker url
    url(r'^save_task/',save_task),#task tracker url
    url(r'^complete_task/',complete_task),# task tracker url
    url(r'^filter_outstanding/',filter_outstanding),# task tracker url
    # url(r'^form-position/$', form_position),


] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
