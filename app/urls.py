from django.conf.urls import url
from django.contrib import admin
from apiAPP import views
from apiAPP import urls
urlpatterns = [
    url(r'^list/$', views.List.as_view()),
    url(r'^add.html', views.Add.as_view()),
    url(r'^update/(\d+)', views.Update.as_view()),
    url(r'^del', views.Del.as_view()),

#    url(r'^apipage$', views.Apilist.as_view()),
    # url(r'^page/$', views.PageTurning.as_view),

]
