import os.path

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

# needed for some admin links (logout...) until http://code.djangoproject.com/ticket/10061 is fixed
admin.site.root_path = '/admin/'

urlpatterns = patterns('',
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^confirm/(?P<id>\d+)/(?P<hash>[^/]+)/$', 'content.views.confirm', name="support_confirm"),
    (r'^$', 'content.views.show_page', { 'slug': 'start', 'form': 'SupporterForm', 'template': 'frontpage.html' }),
    url(r'^(?P<slug>[^/]+)/$', 'content.views.show_page', name="show_page"),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_ROOT, 'media')}),
    )

urlpatterns += patterns('',
    url(r'^tinymce/', include('tinymce.urls')),
)
