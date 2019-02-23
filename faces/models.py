from django.db import models
from django.contrib.auth.models import User
import time

def faces(instance, filename): 
	#print(request.user)
    return "face/%s/%s/%s" %(instance.user,instance,filename)

def video_encoding(instance, filename):
	#print(request.user)
	return "face/%s/%s/%s" %(instance.user,instance,filename)


class Facedetail(models.Model):
	user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	encoding = models.TextField(max_length=1000,blank=True)
	image = models.ImageField(upload_to=faces,blank=True)
	video = models.FileField(upload_to=video_encoding,blank=True)

	def __str__(self):
		return self.name