# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin

from form_addon.models import *
from blero_grid.cms_plugins import BleroGridPlugin
from blero_grid.models import GridCells
from blero_grid.models import PluginPosition as BGPluginPosition
from . import models

# loggin Details#
import logging
import os

# Start Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('form_addon.log')
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)


# class FormInputsInline(admin.StackedInline):
#     model = FormInputs
#     fk_name = 'id_fr'
#
#
# class FormsPlugin(CMSPluginBase):
#     model = FormPlugin
#     name = "Form Addon"
#     render_template = "form_addon/create_form.html"
#     inlines = [FormInputsInline, ]
#
#     # module = _("FormAddon")
#
#     def __init__(self, model=None, admin_site=None):
#         super(FormsPlugin, self).__init__(model=model,
#                                           admin_site=admin_site)
#         for inline in self.inlines:
#             inline.placeholder = self.placeholder
#             inline.page = self.page
#
#     def render(self, context, instance, placeholder):
#         inputs = instance.form_plugin.all()
#
#         context.update({
#             'instance': instance,
#             # 'placeholder': placeholder,
#             'inputs': inputs
#         })
#         return context
#
#
# plugin_pool.register_plugin(FormsPlugin)

class FormInputsInline(admin.StackedInline):
    model = FormInputs
    fk_name = 'id_fr'


class BleroGridFormPlugin(BleroGridPlugin):
    model=BleroGridForm
    name="Form Grid"
    render_template = "/app/blero_grid/templates/blero_grid/grid_base.html"

    def render(self, context, instance, placeholder):
        data = []

        active_grid = BleroGridForm.objects.get(pk=instance.pk)
        grid_values = GridCells.objects.all().filter(model=active_grid)

        cell_data = {}

        for cell in grid_values:
            cell_data[cell.row_number] = {'column_number': cell.column_number, 'cell_content': cell.cell_content}

        columns = int(instance.grid_columns)
        rows=int(instance.grid_rows)
        position = BGPluginPosition.objects.filter(model=instance).first()
        context.update({
            'instance': instance,
            'cell_data': cell_data,
            'position': position,
            'columns': [i for i in range(columns)],
            'rows': [i for i in range(rows)],
        })

        return context

class FormsPlugin(CMSPluginBase):
    model = FormPlugin
    name = "Form Addon"
    render_template = "form_addon/create_form.html"
    inlines = (FormInputsInline,)

    allow_children = True
    child_classes = ['BleroGridFormPlugin']

    # Class plug in should be modified to have two more fields
    # a boolean field that says if it should load a saved model or not
    # text field with a dropdown for the names of the models saved,
    #
    # if the boolean is selected then the full form will be overwriten and rendered with the saved model values.
    # name=savedmode.model.name
    # pyfunction=savedmodel.model.pyfunction
    # ETC, so all the fields of the form pluse the selected securities and dates should be  saved and loaded.

    def __init__(self, model=None, admin_site=None):
        super(FormsPlugin, self).__init__(model=model,
                                          admin_site=admin_site)
        for inline in self.inlines:
            inline.placeholder = self.placeholder
            inline.page = self.page

    def render(self, context, instance, placeholder):
        context = super(FormsPlugin, self).render(context, instance, placeholder)

        instances = instance
        items = FormInputs.objects.filter(id_fr=instance).select_related('inp_position').select_related('label_position')

        position = PluginPosition.objects.filter(model=instance).first()
        context.update({
            'instance': instances,
            'position': position,
            'inputs': items,
        })
        return context


plugin_pool.register_plugin(FormsPlugin)
plugin_pool.register_plugin(BleroGridFormPlugin)
