from django.conf.urls import url

from .. import apis as views

urlpatterns = [
    url(r'^$', views.UserAPI.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetailAPI.as_view()),
    url(r'^login/$', views.LoginAPI.as_view()),
    url(r'^logout/$', views.LogoutAPI.as_view()),
    url(r'^signup/$', views.SignUpAPI.as_view()),
    url(r'^signup-b/$', views.SignUpIosAPI.as_view()),
    url(r'^fb/$', views.FacebookLoginAPI.as_view()),
    url(r'^(?P<pk>[0-9]+)/follow/$', views.FollowAPI.as_view()),
    url(r'^activate/', views.UserActivateAPI.as_view()),
    url(r'^auth-mail/', views.UserAuthMailAPI.as_view()),
]
