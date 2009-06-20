from django.forms import ModelForm

from support.models import Supporter

class SupporterForm(ModelForm):
    class Meta:
        model = Supporter
