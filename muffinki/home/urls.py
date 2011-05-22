from django.conf.urls.defaults import patterns, url

from home import views


urlpatterns = patterns('home.views',
    url(r'^$', 'index', name='home_index')
)
