from django.contrib import admin

from content.models import Text


class TextAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(Text, TextAdmin)