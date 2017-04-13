from django.conf.urls import url

from .. import apis as views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.UserProfileViewAPI.as_view()),
    url(r'^login/', views.LoginAPI.as_view()),
    url(r'^logout/', views.LogoutAPI.as_view()),
    url(r'^signup/', views.SignUpAPI.as_view()),
<<<<<<< HEAD
=======
    url(r'^fb/', views.FacebookLoginAPI.as_view()),
>>>>>>> bc95b67aef65e6f984d661d45e80409205842039
]
