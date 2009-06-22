from django import template
from django.conf import settings
from django.db import models

from altendorfdsl.support.models import Supporter

register = template.Library()


@register.simple_tag
def get_supporter_count():
    return Supporter.objects.filter(verified=True).count()
