# vim: et ts=4 sw=4
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myfeeder.views.home', name='home'),
    # url(r'^myfeeder/', include('myfeeder.foo.urls')),

    url(r'^reader/', include('reader.urls')),
    #url(r'^reader/', include('feincms.urls')),
    #url(r'', include('feincms.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
