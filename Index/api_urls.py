from django.urls import path
from django.urls import include
from Index.views import *
# from django.conf import settings
from . import views
from django.conf.urls import url
# app_name = 'Index'


urlpatterns = [
	url('addcameraapi/',AddcameraAPI),
	url('notificationapi/',NotificationAPI),
	# url('addcameraapi_details/',AddcameraAPI_details),
	# url('Index/', Index),
	url('addcameraapi_details/<int:id>/', AddcameraAPI_details),
	# url('Notification', Notification),
	# url('Notification/<int:id>/', Notification_details)
]
