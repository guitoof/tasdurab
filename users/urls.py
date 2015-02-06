from django.conf.urls import patterns, url

from users.views import UserDetailView, UserUpdateView

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', UserDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/register$', UserUpdateView.as_view(), name='register'),
)
