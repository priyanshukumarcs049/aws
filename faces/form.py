from django import forms

from .models import Facedetail
'''
class LocationForm(forms.ModelForm):
	place = forms.CharField(max_length=128, help_text="Please enter the category name.")
	class Meta:
		model = Location
		fields = ('place',)
'''
class FacedetailForm(forms.ModelForm):
	# name = models.CharField(max_length=30)
	# encoding = models.TextField(max_length=1000,blank=True)
	# image = models.ImageField(upload_to=faces,blank=True)
	# video = models.FileField(upload_to=video_encoding,blank=True)
	name = forms.CharField(max_length=30, help_text= "Please enter the category name.")
	encoding = forms.CharField(max_length=1000, help_text="Pleas enter the category name")


	class Meta:
		model = Facedetail

		fields = ('name', 'encoding','image','video')

