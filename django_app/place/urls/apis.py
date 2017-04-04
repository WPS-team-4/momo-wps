from django.conf.urls import url
from .. import apis as views

urlpatterns = [
    url(r'^$', views.PlaceList.as_view(), name='place-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PlaceDetail.as_view(), name='place-detail'),
]