from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', include('home.urls')),


    url(r'^_admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^_admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # serve static files when in debug mode
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()