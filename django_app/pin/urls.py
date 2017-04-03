from django.conf.urls import url

from . import views

app_name = 'pin'
urlpatterns = [
    url(r'^$', views.add_pin, name='add-pin'),
]
