from rest_framework import serializers
# from django.contrib.auth.models import Camera
from Index.models import Camera, Notification

class CameraSerializer(serializers.ModelSerializer):
	class Meta:
		model = Camera
		fields = [
			"id",
			"ip",
			"name",
			"user"
			]
class NotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notification
		fields = [
			"id",
			"name",
			"place",
			"time",
			"user"
			]
