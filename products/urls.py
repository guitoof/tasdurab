from django.conf.urls import patterns, url

from products import views

urlpatterns = patterns('',
    url(r'^$', views.ProductListView.as_view(), name='index'),
    url(r'create/$', views.ProductCreateView.as_view(), name='create'),
)
