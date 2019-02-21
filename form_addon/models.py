# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from cms.models import CMSPlugin
from dateutil.parser import parse
# loggin Details#
import logging
from blero_grid.models import  BleroGrid

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

@python_2_unicode_compatible
class FormPlugin(CMSPlugin):

    FORM_CHOICES = (
        ('new', 'New Form'),
        ('load', 'Load Form'),

    )




    #inputs to load or create new form
    # Decomment to activate load model
    #load_form = models.CharField(choices=FORM_CHOICES, max_length=250, null=True, blank=True,default='new')
    #model_name = models.CharField(max_length=250, null=True, blank=True)
    #######

    form_name = models.CharField(max_length=250, null=True, blank=True)
    button_name = models.CharField(max_length=250, null=True, blank=True)
    ajax_function = models.CharField(max_length=250, null=True, blank=True)
    py_function = models.CharField(max_length=250, null=True, blank=True)

    def copy_relations(self, oldinstance):
        self.form_plugin.all().delete()

        for input in oldinstance.form_plugin.all():
            input.pk = None
            input.id_fr = self
            input.save()
    def __str__(self):
        return self.form_name + " id: " +str(self.pk)

    class Meta:
        verbose_name = 'Addon Form New'
        verbose_name_plural = 'Addon Forms New'


@python_2_unicode_compatible
class FormInputs(models.Model):
    STATUS_CHOICES = (
        ('text', 'TextBox'),
        ('date', 'Date Field'),
        ('checkbox', 'Checkbox'),
    )
    id_fr = models.ForeignKey(FormPlugin, related_name="form_plugin")
    input_name = models.CharField(max_length=100, null=True, blank=True)
    input_type = models.CharField(choices=STATUS_CHOICES, max_length=250, null=True, blank=True)
    input_value = models.CharField(max_length=250, verbose_name="Default Value", null=True, blank=True)

    class Meta:
        verbose_name = 'New Field'
        verbose_name_plural = 'New Fields'

#Uncomment to activate Save/Store Model
# class StoreModels(models.Model):
#     ajax_function = models.CharField(max_length=250, null=True, blank=True)
#     py_function = models.CharField(max_length=250, null=True, blank=True)
#     regressors = models.CharField(max_length=250, null=True, blank=True)
#     target = models.CharField(max_length=250, null=True, blank=True)
#     model_name = models.CharField(max_length=250, null=True, blank=True)
#     form_name = models.CharField(max_length=250, null=True, blank=True)
#     model_comments = models.CharField(max_length=250, null=True, blank=True)
#     button_name = models.CharField(max_length=250, null=True, blank=True)
#     from_date = models.CharField(max_length=250, null=True, blank=True)
#     to_date = models.CharField(max_length=250, null=True, blank=True)
#
#     def __str__(self):
#         return self.model_name


class ModelsInput(models.Model):
    STATUS_CHOICES = (
        ('text', 'TextBox'),
        ('date', 'Date Field'),
        ('checkbox', 'Checkbox'),
    )
    #decoment to activate load/get_model
    #model = models.ForeignKey(StoreModels)
    input_name = models.CharField(max_length=100, null=True, blank=True)
    input_type = models.CharField(choices=STATUS_CHOICES, max_length=250, null=True, blank=True)
    input_value = models.CharField(max_length=250, verbose_name="Default Value", null=True, blank=True)

    def __str__(self):
        return self.input_name


#child models

class BleroGridForm(BleroGrid):
    parent_form=models.ForeignKey(FormPlugin,on_delete=models.CASCADE)


#Models for position
class PluginPosition(models.Model):#FormSavePosition
    model = models.ForeignKey(FormPlugin,on_delete=models.CASCADE)
    is_resized = models.BooleanField(default=False)
    width = models.CharField(max_length=50, null=True)
    height = models.CharField(max_length=50, null=True)
    top = models.CharField(max_length=50, null=True)
    left = models.CharField(max_length=50, null=True)


class InputPluginPosition(models.Model):
    model = models.OneToOneField(FormInputs, on_delete=models.CASCADE, related_name="inp_position")
    is_resized = models.BooleanField(default=False)
    width = models.CharField(max_length=50, null=True)
    height = models.CharField(max_length=50, null=True)
    top = models.CharField(max_length=50, null=True)
    left = models.CharField(max_length=50, null=True)


class LabelPluginPosition(models.Model):
    model = models.OneToOneField(FormInputs, on_delete=models.CASCADE, related_name="label_position")
    is_resized = models.BooleanField(default=False)
    width = models.CharField(max_length=50, null=True)
    height = models.CharField(max_length=50, null=True)
    top = models.CharField(max_length=50, null=True)
    left = models.CharField(max_length=50, null=True)


class FormBtnPluginPosition(models.Model):
    model = models.OneToOneField(FormPlugin, on_delete=models.CASCADE, related_name="btn_position")
    is_resized = models.BooleanField(default=False)
    width = models.CharField(max_length=50, null=True)
    height = models.CharField(max_length=50, null=True)
    top = models.CharField(max_length=50, null=True)
    left = models.CharField(max_length=50, null=True)
