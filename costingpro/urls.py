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
    url(r"^update_profile/$", "dashboard.views.update_profile", name ="update_profile"),
    url(r"^update_profile_success/$", "dashboard.views.update_profile_success", name="update_profile_success"),
    url(r'^accounts/signup/$', 'dashboard.views.signup', name='signup'),
	url(r'^business_profile/new/$', 'dashboard.views.business_profile', name='business_profile_new'),
	url(r'^business_profile/(?P<pk>\d+)/$', 'dashboard.views.business_profile_detail',
			name='business_profile_detail'),
	url(r'^business_profile/(?P<pk>\d+)/new-inventory/$', 
		 'dashboard.views.new_inventory', name='new_inventory'),
	# products
	url(r'^business_profile/(?P<pk>\d+)/new-product/$', 
		 'dashboard.views.new_product', name='new_product'),
	url(r'^business_profile/(?P<pk>\d+)/products/$', 
		 'dashboard.views.products', name='products'),
	url(r'^all-products/$', 'dashboard.views.all_products', name='all_products'),
	url(r'^business_profile/(?P<pk>\d+)/products/(?P<id>\d+)$', 
		 'dashboard.views.product', name='product'),

	url(r'^business_profile/(?P<pk>\d+)/products/(?P<id>\d+)/add-raw-material/$', 
		 'dashboard.views.product_add_raw_material', name='product_add_raw_material'),
	# end products

	url(r'^business_profile/(?P<pk>\d+)/raw-materials/$', 
		'dashboard.views.costing_raw_materials', name='costing_raw_materials'),
	url(r'^business_profile/(?P<pk>\d+)/raw-materials/(?P<id>\d+)/$', 'dashboard.views.costing_detail', name='costing_detail'),
	# url(r'^business_profile/(?P<pk>\d+)/raw-materials/(?P<id>\d+)/edit/$', 
		# 'dashboard.views.raw_material_edit', name='raw_material_edit'),
	url(r'^menu/$', 'dashboard.views.menu', name='menu'),
	url(r'^business_profile_list/$', 'dashboard.views.business_profile_list', name='business_profiles'),
	

    url(r'^admin/', include(admin.site.urls)),
 )
