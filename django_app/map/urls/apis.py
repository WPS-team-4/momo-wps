from django.conf.urls import url

from .. import apis as views

urlpatterns = [
    url(r'^$', views.MapList.as_view(), name='pin-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.MapDetail.as_view(), name='pin-detail'),
]
