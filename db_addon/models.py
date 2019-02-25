from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from cms.models import CMSPlugin
from dateutil.parser import parse


@python_2_unicode_compatible
class DBPlugin(CMSPlugin):

    # FORM_CHOICES = (
    #     ('new', 'New Form'),
    #     ('load', 'Load Form'),
    #
    # )

    # #inputs to load or create new form
    # load_form = models.CharField(choices=FORM_CHOICES, max_length=250, null=True, blank=True,default='new')
    # model_name = models.CharField(max_length=250, null=True, blank=True)
    # #######

    label = models.CharField(
        blank=True,
        max_length=200,
    )

    def __str__(self):
        return self.label




@python_2_unicode_compatible
class DBPlugin_individual(CMSPlugin):


    database_name = models.CharField(max_length=250, null=True, blank=True)
    database_table_name = models.CharField(max_length=250, null=True, blank=True)
    database_filter_column = models.CharField(max_length=250, null=True, blank=True)
    database_py_function = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return self.database_name or self.database_table_name








