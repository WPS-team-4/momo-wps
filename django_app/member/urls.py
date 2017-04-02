from django.conf.urls import url

from member import views

urlpatterns = [
    url(r'^login/', views.LoginAPI.as_view()),
]
