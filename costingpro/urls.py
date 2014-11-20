from django.conf.urls import patterns, include, url
from django.contrib import admin
from dashboard import views




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'costingpro.views.home', name='home'),   
    url(r'^accounts/', include('reg.urls')),
	url(r'^$', 'dashboard.views.home', name='index'),
	url(r'^business-profile/$', 'dashboard.views.business_profile', name='business_profile'),
	url(r'^menu/$', 'dashboard.views.menu', name='menu'),
    url(r'^admin/', include(admin.site.urls)),
 )
