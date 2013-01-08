from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'acadereg.views.home', name='home'),
    # url(r'^acadereg/', include('acadereg.foo.urls')),
    url(r'^', include('alumnos.urls')),
    url(r'^', include('institucional.urls')),
    url(r'^subir/(?P<path>.*)$','django.views.static.serve',{'documen_root':settings.MEDIA_ROOT }),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
