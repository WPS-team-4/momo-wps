from django.conf.urls import url

from .. import apis as views

urlpatterns = [
    url(r'^$', views.SearchMapAndUserAPI.as_view(), name='main-search'),
]