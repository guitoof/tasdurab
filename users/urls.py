from django.conf.urls import patterns, url

from users.views import UserDetailView, UserCreateView

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', UserDetailView.as_view(), name='detail'),
    url(r'register$', UserCreateView.as_view(), name='create'),
)
