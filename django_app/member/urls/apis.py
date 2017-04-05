from django.conf.urls import url

from .. import apis as views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.UserProfileViewAPI.as_view()),
    url(r'^login/', views.LoginAPI.as_view()),
    url(r'^logout/', views.LogoutAPI.as_view()),
    url(r'^signup/', views.SignUpAPI.as_view()),
]
