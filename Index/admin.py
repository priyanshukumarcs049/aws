from django.contrib import admin

from . import models


class CameraAdmin(admin.ModelAdmin):
	list_display = ('name', 'ip')
	empty_value_display = 'unknown'
'''
class LocationAdmin(admin.ModelAdmin):
	list_display = ('id', 'place')
	empty_value_display = 'unknown'
'''
#admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Camera, CameraAdmin)
admin.site.register(models.Notification)
admin.site.register(models.Profile)
#admin.site.unregister(User)
#admin.site.register(models.Userprofile)
