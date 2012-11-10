from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('main.views',
     url(r'^$', 'index', name='index'),
     url(r'^about/$', 'about', name='about'),
)
