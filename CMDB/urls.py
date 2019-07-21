"""CMDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from app import views
from apiAPP import urls
from app import urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
   # url(r'^login/$', views.Login.as_view()),
   # url(r'^register/$', views.register),
    #url(r'^index/', views.Index.as_view()),
    #url(r'^session/', views.Session),
    #url(r'^logout/', views.del_session),
    #调用redirect
    #(r'dump/$',views.dump),
    url(r'^api/', include('apiAPP.urls')),
    url(r'^cmdb/', include('app.urls')),
]
