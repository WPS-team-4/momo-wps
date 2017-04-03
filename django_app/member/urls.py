from django.conf.urls import url

from member import views

urlpatterns = [
    url(r'^profile/', views.UserProfileViewAPI.as_view()),
    url(r'^login/', views.LoginAPI.as_view()),
]
