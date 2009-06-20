from django.contrib import admin

from support.models import Supporter


class SupporterAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'strasse', 'plz', 'ort', 'verified')

admin.site.register(Supporter, SupporterAdmin)