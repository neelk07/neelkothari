from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from blog.models import Post
from blog.views import *



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'neelkothari.views.home', name='home'),
    # url(r'^neelkothari/', include('neelkothari.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', landing_page),
    url(r'^blog/', blog),
    url(r'^profile/', profile),

)
