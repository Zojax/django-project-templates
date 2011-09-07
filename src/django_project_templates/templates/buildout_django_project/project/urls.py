from django.conf import settings
from django.conf.urls.defaults import patterns, include, handler404, \
    url
from django.contrib import admin
from project.views import handler500

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'project.views.index_view',
        name='home'),
)

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots.txt$', include('robots.urls')),
)

