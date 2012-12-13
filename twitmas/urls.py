from django.conf.urls import patterns, include, url
from twitmas.views import TwitmasView, get_tweet

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitmas.views.home', name='home'),
    # url(r'^twitmas/', include('twitmas.foo.urls')),

    url(r'^$', TwitmasView.as_view()),

    url(r'^get_tweet/$', get_tweet),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
