from django.conf.urls import patterns, include, url
from django.contrib import admin
from dashboard import views
from registration.backends.simple.views import RegistrationView



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'costingpro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),    
    url(r'^accounts/', include('reg.urls')),
	url(r'^$', 'dashboard.views.home', name='index'),
    url(r'^admin/', include(admin.site.urls)),
 )
