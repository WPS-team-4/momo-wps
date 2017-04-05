from django.conf.urls import url

from . import views

app_name = 'pin'
urlpatterns = [
    url(r'^$', views.create_pin, name='create-pin'),
]
