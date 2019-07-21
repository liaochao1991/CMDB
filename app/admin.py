from django.contrib import admin
from app import models

# Register your models here.
admin.site.register(models.AdminInfo)
admin.site.register(models.UserProfile)
admin.site.register(models.UserGroup)
admin.site.register(models.Disk)
admin.site.register(models.Asset)
admin.site.register(models.BusinessUnit)
admin.site.register(models.ErrorLog)
admin.site.register(models.Memory)
admin.site.register(models.IDC)