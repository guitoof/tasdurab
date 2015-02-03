from django.conf.urls import patterns, url

from users.views import UserDetailView

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', UserDetailView.as_view(), name='detail'),
)
