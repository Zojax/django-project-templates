from authentication.forms import ChallengeQuestionEmailAuthenticationForm
from django.conf import settings
from django.conf.urls.defaults import patterns, include, handler404, \
    url
from django.contrib import admin
from project.custom.registration.forms import RegistrationForm
from satchmo_store.urls import urlpatterns as satchmo_urlpatterns
from project.custom.registration.urls import urlpatterns as registration_urlpatterns
from project.views import handler500

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^accounts/login/?$', 'authentication.views.emaillogin',
        {'template_name': 'registration/login.html'},
        name='auth_login'),
    url(r'^$', 'project.views.index_view',
        name='home'),
)

urlpatterns += satchmo_urlpatterns

urlpatterns += patterns(
    '',
    url(r'^admin/filebrowser/?$', 'filebrowser.views.browse', name='filebrowser-index'),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^adminfiles/', include('adminfiles.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^kss/', include('kss.django.urls')),
    url(r'^accounts/', include("profile.urls")),
    url(r'^vdr/', include('vdr.urls')),
    url(r'^plans/?$', 'vdr.views.plans', name='plans'),
    url(r'^support/?$', 'vdr.views.support', name='support'),
    url(r'^mailin/', include('zojax.django.mailin.urls')),
    url(r'^robots.txt$', include('robots.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += registration_urlpatterns

urlpatterns += patterns('',
    url(r'^', include('pages.urls')),
)

