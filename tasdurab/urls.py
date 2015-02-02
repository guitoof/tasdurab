from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('products.urls', namespace='products')),
    url(r'^products', include('products.urls', namespace='products')),
    url(r'^login$', 'django_cas_ng.views.login', name='login'),
    url(r'^logout$', 'django_cas_ng.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
