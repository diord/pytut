from django.contrib import admin
admin.autodiscover()
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from newproj.views import hello, current_datetime, hours_ahead, about

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    ('^$', hello),
    ('^hello/$', hello),
	('^time/$', current_datetime),
	('^about/$', about),
	(r'^time/plus/(\d{1,2})/$', hours_ahead)
    # Examples:
    # url(r'^$', 'newproj.views.home', name='home'),
    # url(r'^newproj/', include('newproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
