from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'nostrikesite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^get_pois/', 'mapapp.views.get_pois', name='get_pois'),
    url(r'^add_poi/', 'mapapp.views.add', name='add_poi'),
)
