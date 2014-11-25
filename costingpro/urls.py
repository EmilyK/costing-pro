from django.conf.urls import patterns, include, url
from django.contrib import admin
from dashboard import views




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'costingpro.views.home', name='home'),   
    #url(r'^accounts/', include('reg.urls')),
	url(r'^$', 'dashboard.views.home', name='index'),
	url(r'^accounts/login/$', 'dashboard.views.login', name='login'),
	url(r'^accounts/auth_view/$', 'dashboard.views.auth_view', name='auth_view'),
	url(r'^accounts/signup/$', 'dashboard.views.signup', name='signup'),
	url(r'^business_profile/$', 'dashboard.views.business_profile', name='business_profile'),
	url(r'^business_profile/costing/$', 'dashboard.views.costing', name='costing'),
	url(r'^menu/$', 'dashboard.views.menu', name='menu'),
    url(r'^admin/', include(admin.site.urls)),
 )
