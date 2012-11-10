from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.index', name='index'),
    url(r'^kontakt/$', TemplateView.as_view(template_name="contact.html"), name='contact'),
    url(r'^admin/', include(admin.site.urls)),
)
