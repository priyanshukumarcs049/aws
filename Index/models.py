from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
#from accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
from phonenumber_field.modelfields import PhoneNumberField

phonenumber = PhoneNumberField(blank=True)

# class Userprofile(models.Model):
# 	user = models.OneToOneField(User,on_delete=models.CASCADE)
# 	phone = models.IntegerField()
#
# 	def __str__(self):
# 		return self.phone


class Camera(models.Model):
	ip = models.CharField(max_length=500,null=False,blank=False,unique=True)
	name = models.CharField(max_length=500,null=False,blank=False)
	user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
	#option = models.CharField(max_length=20)
	#auth_uname = models.CharField(max_length=200)
	#uth_pwd = models.CharField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	created_at = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.name



class Notification(models.Model):
	user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	place = models.CharField(max_length=50)
	time = models.CharField(max_length=50)

	def __str__(self):
		return self.name
def profile_image(user, filename):
    return "userpics/%s/%s" %(str(user)+str(int(time.time())),filename)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=30)
	MALE = 'MA'
	FEMALE = 'FE'
	GENDERS_IN_PROJECT = (
	(MALE, 'male'),
	(FEMALE, 'female'),
	)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	gender = models.CharField(max_length=2,choices=GENDERS_IN_PROJECT,default=MALE)
	phone = PhoneNumberField(default=0,blank=True,null=True)
	email = models.EmailField(max_length=50,blank=True)
	image = models.ImageField(upload_to=profile_image,blank=True)
	image.allow_tags = True

	def __str__(self):
		return self.fullname

	def get_absolute_url(self):
		return reverse('Index:profiledetail',kwargs={'pk':self.pk})

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
