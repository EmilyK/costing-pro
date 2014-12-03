from django.conf.urls import patterns, include, url
from django.contrib import admin
from dashboard import views




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'costingpro.views.home', name='home'),   
    #url(r'^accounts/', include('reg.urls')),
	url(r'^$', 'dashboard.views.home', name='index'),
    url(r"^login/$", "dashboard.views._login"),
    url(r"^logout/$", "django.contrib.auth.views.logout"),
    url(r'^accounts/signup/$', 'dashboard.views.signup', name='signup'),
	url(r'^business_profile/new/$', 'dashboard.views.business_profile', name='business_profile_new'),
	# TODO -> be able to get a single business profile in case of M2M relationship
	url(r'^business_profile/(?P<pk>\d+)/new-inventory/$', 
		 'dashboard.views.new_inventory', name='new_inventory'),
	url(r'^business_profile/(?P<pk>\d+)/raw-materials/$', 
		'dashboard.views.costing_raw_materials', name='costing_raw_materials'),
	url(r'^business_profile/(?P<pk>\d+)/raw-materials/(?P<id>\d+)/$', 'dashboard.views.costing_detail', name='costing_detail'),
	# url(r'^business_profile/(?P<pk>\d+)/raw-materials/(?P<id>\d+)/edit/$', 
		# 'dashboard.views.raw_material_edit', name='raw_material_edit'),
	url(r'^menu/$', 'dashboard.views.menu', name='menu'),
	url(r'^business_profile_list/$', 'dashboard.views.business_profile_list', name='business_profiles'),


    url(r'^admin/', include(admin.site.urls)),
 )
