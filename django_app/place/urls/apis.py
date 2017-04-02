from django.conf.urls import url
from .. import apis
urlpatterns = [
    url(r'^search/$', apis.SearchPlaceView.as_view(), name='search-place'),
    url(r'^resist/$', apis.ResistPlaceView.as_view(), name='resist-place'),
]