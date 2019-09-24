
from django.conf.urls import url,include
from django.contrib import admin
from auth_server import views
from auth_server import urls
urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    url(r'^user/list.html', views.List.as_view()),
    url(r'^user/add.html$', views.Add.as_view()),
    url(r'^user/(\d+)/update.html', views.Update.as_view()),
    url(r'^user/(\d+)/del.html', views.Del.as_view()),
]
