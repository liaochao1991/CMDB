from django.contrib import admin
from apiAPP import models
# Register your models here.

# class Myadmin(admin.ModelAdmin):
#     #控制前端显示字段
#     list_display = ("username","password")
# admin.site.register(models.Userinfo,Myadmin)
'''
    注册到admin
'''
admin.site.register(models.Userinfo)
admin.site.register(models.Position)
admin.site.register(models.Auth)
admin.site.register(models.AuthGroup)
admin.site.register(models.Menu)
