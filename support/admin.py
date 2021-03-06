from django.contrib import admin

from support.models import Supporter


class SupporterAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'strasse', 'plz', 'ort', 'verified', 'date_registered',)
    list_filter = ('verified',)

admin.site.register(Supporter, SupporterAdmin)