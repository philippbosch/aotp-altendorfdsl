from django.db import models
from django.utils.translation import ugettext as _

from tinymce.models import HTMLField

class Text(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    text = HTMLField(verbose_name=_("Text"))
    slug = models.SlugField(verbose_name=_("Slug"))
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name="Text"
        verbose_name_plural="Texte"