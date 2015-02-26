from django.conf.urls import patterns, url

from products import views

urlpatterns = patterns('',
    url(r'^$', views.ProductListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='detail'),
    url(r'login/create/$', views.ProductCreateView.as_view(), name='create'),
)
