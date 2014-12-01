from django.conf.urls import patterns, include, url
from django.contrib import admin
from dashboard import views




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'costingpro.views.home', name='home'),   
    #url(r'^accounts/', include('reg.urls')),
	url(r'^$', 'dashboard.views.home', name='index'),
    url(r"^login/$", "django.contrib.auth.views.login"),
    url(r"^logout/$", "django.contrib.auth.views.logout"),
	#url(r'^accounts/login/$', 'dashboard.views.login', name='login'),
	#url(r'^accounts/auth_view/$', 'dashboard.views.auth_view', name='auth_view'),
	url(r'^accounts/signup/$', 'dashboard.views.signup', name='signup'),
	url(r'^business_profile/$', 'dashboard.views.business_profile', name='business_profile'),
	# TODO -> be able to get a single business profile in case of M2M relationship
	url(r'^business_profile/costing/$', 'dashboard.views.costing', name='costing'),
	url(r'^business_profile/(?P<pk>\d+)/costing/raw-materials/$', 
		'dashboard.views.costing_raw_materials', name='costing_raw_materials'),
	url(r'^costing/costing_detail/(?P<pk>\d+)/$', 'dashboard.views.costing_detail', name='costing_detail'),
	url(r'^menu/$', 'dashboard.views.menu', name='menu'),

    url(r'^admin/', include(admin.site.urls)),
 )
