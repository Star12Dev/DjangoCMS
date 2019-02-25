from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from cms.models import CMSPlugin

# Create your models here.

@python_2_unicode_compatible
class BleroContainer(CMSPlugin):


    container_name = models.CharField(
        blank=False,
        max_length=200,
    )

    number_columns=models.CharField(blank=False,max_length=200,)

    def __str__(self):
        return self.container_name


class PluginPosition(models.Model):#FormSavePosition
    model = models.ForeignKey(BleroContainer,on_delete=models.CASCADE)
    is_resized = models.BooleanField(default=False)
    width = models.CharField(max_length=50, null=True)
    height = models.CharField(max_length=50, null=True)
    top = models.CharField(max_length=50, null=True)
    left = models.CharField(max_length=50, null=True)
