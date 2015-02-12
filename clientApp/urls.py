from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import load_contact


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clientApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', load_contact),
)
