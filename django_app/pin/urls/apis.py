from django.conf.urls import url

from .. import apis as views


urlpatterns = [
    url(r'^$', views.PinList.as_view(), name='pin-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PinDetail.as_view(), name='pin-detail'),
    # url(r'^pin/$', views.PinCreate.as_view(), name='pin-create'),
    # url(r'^pin/(?P<pk>[0-9]+)/$', views.PinDestroy.as_view(), name='pin-destroy'),
]
