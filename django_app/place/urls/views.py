from django.conf.urls import url

from place import views

app_name = 'place'
urlpatterns = [
    url(r'^$', views.search, name='search'),
]
