"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# API (JSONResponse)를 위한 urls
from map.urls import apis as map_apis_urls
from member.urls import apis as member_apis_urls
from place.urls import apis as place_apis_urls

# HttpRequest / HttpResponse를 위한 urls
from place.urls import views as place_views_urls

api_urlpatterns = [
    url(r'^member/', include(member_apis_urls)),
    url(r'^map/', include(map_apis_urls)),
    url(r'^place/', include(place_apis_urls)),
    # url(r'^pin/', include(pin_apis_urls)),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include(place_views_urls)),
    # url(r'^pin/', include('pin.urls')),
    url(r'^api/', include(api_urlpatterns, namespace='api'))

]
