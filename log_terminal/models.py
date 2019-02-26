from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from cms.models import CMSPlugin

# Create your models here.


@python_2_unicode_compatible
class LogTerminal(CMSPlugin):

    # terminal_lines = models.CharField(max_length=250, null=True, blank=True)
    terminal_lines = models.CharField(max_length=250, null=False,default=100)

    def __str__(self):
        return 'LogTerminal'


class PluginPosition(models.Model):
    model = models.ForeignKey(LogTerminal,on_delete=models.CASCADE)
    is_resized = models.BooleanField(default=False)
    width = models.CharField(max_length=50, null=True)
    height = models.CharField(max_length=50, null=True)
    top = models.CharField(max_length=50, null=True)
    left = models.CharField(max_length=50, null=True)
