from django.conf.urls import url

from .. import apis as views


urlpatterns = [
    url(r'^$', views.PinListAPI.as_view(), name='pin-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PinDetailAPI.as_view(), name='pin-detail'),
]
