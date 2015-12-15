"""radius URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

from freeradius import views as FreeRadiusView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/userdata/', FreeRadiusView.UserDataList.as_view()),
    url(r'^api/v1/auth/', include('rest_framework.urls',
		namespace='rest_framework')),
    url(r'^api/v1/token/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/v1/token/refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
]

urlpatterns = format_suffix_patterns(urlpatterns)