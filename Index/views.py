from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import StreamingHttpResponse,HttpResponse, HttpResponseRedirect, JsonResponse
from Index.camera import VideoCamera
from .models  import Camera,Notification,Profile
from . import models
from Index.form   import CameraForm, ProfileForm
from urllib.request import urlopen
import cv2
import random
import sys
import string
from django.views.generic import View,TemplateView ,ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
import time,datetime
from django.views import View
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView ,UpdateView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from Index.serializers import CameraSerializer ,NotificationSerializer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
import json
from collections import OrderedDict
@csrf_exempt
def AddcameraAPI(request):
    context={}
    user_id=request.user
    id=user_id.id
    if request.method == "GET":
        cameras = Camera.objects.filter(user_id=id)
        serializer = CameraSerializer(cameras, many=True)
        print(json.dumps(serializer.data))
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = CameraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            cameras = Camera.objects.filter(user_id=id)
            serializer1 = CameraSerializer(cameras, many=True)
            return JsonResponse(json.dumps(serializer.data),safe=False)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def AddcameraAPI_details(request, id):
	context={}
	user_id=request.user
	id=user_id.id
	try:
		instance = Camera.objects.get(id=id)
	except Camera.DoesNotExist as e:
		return JsonResponse( {"error": "The Data are You trying to find is not Valid."}, status= 404)

	if request.method == "GET":
		cameras = Camera.objects.filter(user_id=id)
		serializer = CameraSerializer(cameras, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == "POST":
		json_parser = JSONParser()
		data = json_parser.parse(request)
		serializer = CameraSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def NotificationAPI(request):
	context={}
	user_id=request.user
	id=user_id.id

	if request.method == "GET":
		notifications = Notification.objects.filter(user_id=id)
		serializer = NotificationSerializer(notifications, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == "POST":
		json_parser = JSONParser()
		data = json_parser.parse(request)
		serializer = NotificationSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=202)
		return JsonResponse(serializer.errors, status=500)

@csrf_exempt
def NotificationAPI_details(request, id):
	context={}
	user_id=request.user
	id=user_id.id
	try:
		instance = Notification.objects.get(id=id)
	except Notification.DoesNotExist as e:
		return JsonResponse( {"error": "The Data are You trying to find is not Valid."}, status= 404)

	if request.method == "GET":
		notifications = Notification.objects.filter(user_id=id)
		serializer = NotificationSerializer(notifications, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == "POST":
		json_parser = JSONParser()
		data = json_parser.parse(request)
		serializer = NotificationSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

# def home(request):
# 	return render(request,'home.html')
@login_required
def home(request):
    user=request.user
    #id=user_id.id
    print(user.profile.phone)
    #profile=Profile.objects.filter(user_id=id)
    if user.profile.phone is None:
        message11 = 'alert'
        return render(request,'home.html',{'message11':message11})
    else:
        count = User.objects.count()
        return render(request, 'home.html', {
        'count': count
        })

class AddcameraView(SuccessMessageMixin, CreateView):
	fields = ('ip','name')
	model = Camera
	template_name='Index/Camera_Add.html'
	#success_url = ''
	#success_message = "Camera Details successfully created!"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AddcameraView, self).dispatch(*args, **kwargs)

	# def get_success_message(self,cleaned_data):
	# 	print(cleaned_data)
	# 	return 'Camera Details successfully created!'
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		#messages.success(request, 'details updated Successfully')
		return redirect('Index:home')#http.HttpResponseRedirect(self.get_success_url())
	# def get_context_data(self, *args, **kwargs):
	# 	context = super(AddcameraView, self).get_context_data(*args, **kwargs)
	# 	context['message'] = 'Camera Added Successfully'
	# 	return context


# @login_required
# def addcamera(request):
# 	user_id = request.user
# 	id=user_id.id
# 	context = {}
#
# 	if request.method == "POST":
# 		ip = request.POST['ip']
# 		name = request.POST['name']
# 		auth_uname = request.POST['auth_uname']
# 		auth_pwd   = request.POST['auth_pwd']
# 		location = User.objects.get(pk=id)
#
# 		camObj = Camera.objects.create(
# 									ip=ip,
# 									name=name,
# 									user = location,
# 									auth_uname = auth_uname,
# 									auth_pwd = auth_pwd
# 								)
#
# 		camObj.save()
# 		Camname = Camera.objects.all()
# 		context.update({'Camname':Camname,'locations':location})
#
# 		return render (request,"home.html",context)
#
# 	context.update({})
#
# 	return render (request,"Index/Camera_Add.html",context)

def gen(camera,CamName,camID1,id):
	while True:
		frame = camera.get_frame(CamName,camID1,id)
		yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n' )

@login_required
def video_streamer(request, camID ):
    camObj = Camera.objects.get(pk=camID)
    user_id=request.user
    id1=user_id.id
    id =  User.objects.get(pk=id1)
    camIP = "%s" %(camObj.ip)
    repsone = gen(VideoCamera(camIP),camObj.name,camID,id)
    return  StreamingHttpResponse(repsone,content_type='multipart/x-mixed-replace; boundary=frame')

class LiveView(ListView):
	context_object_name = 'CameraLists'
	template_name = "Index/cameras.html"
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LiveView, self).dispatch(*args, **kwargs)

	def get_queryset(self):
		return Camera.objects.filter(user=self.request.user)

@login_required
def cameradetails(request):
	context={}
	user_id=request.user
	id=user_id.id
	cameradetail = Camera.objects.filter(user_id=id)
	context.update({'cameradetail':cameradetail })
	return render(request,'Index/cameradetail.html',context)

@login_required
def cameras_list(request):
	context = {}
	user_id=request.user
	id=user_id.id
	CameraLists = Camera.objects.filter(user_id=id)
	context.update({'CameraLists' : CameraLists})
	return render(request,"Index/cameras.html",context)


@login_required
def deletecamera(request):
	user_id=request.user
	id=user_id.id
	context = {}

	if request.method == "POST":

		name = request.POST['name1']
		location =  User.objects.get(pk=id)
		camObj = Camera.objects.get(
									id=name,
									user=location
								)

		camObj.delete()
		Camname = Camera.objects.all()
		message = 'camera Deleted Successfully'
		context.update({'Camname':Camname,'mess':message})

		return render (request,"home.html",context)

	locations = Camera.objects.filter(user_id=id)

	context.update({'locations' : locations})

	return render (request,"Index/camera_delete.html",context)


def notification(request):
	user_id=request.user
	id=user_id.id
	context = {}
	noti = Notification.objects.filter(user_id=id)[::-1]
	context.update({'noti' : noti})
	return render (request,"Index/notification.html",context)

def image(request):
	return render(request,'Index/image.html')


# def sample11(request):
#     context={}
#     if request.method == "POST":
#         print(time.time())
#         camObj = Notification.objects.create(
# 									a='fsvd',
# 									b='sda',
# 									c = 'sadsa',
# 									d = str(datetime.datetime.now().time())
# 								        )
#         camObj.save()
#         print(time.time())
#         return render(request,'Index/sample11.html',context)
#     return render(request,'Index/sample11.html',context)

class ProfileDetailView(DetailView):
	#fields = ('fullname','location','birth_date','gender','phone','image')
	model = models.Profile
	template_name = 'Index/profile.html'

	#@method_decorator(login_required)
	# def dispatch(self, *args, **kwargs):
	# 	return super(ProfileUpdateView, self).dispatch(*args, **kwargs)
	#
	# def form_valid(self, form):
	# 	obj = form.save(commit=False)
	# 	obj.user = self.request.user
	# 	obj.save()
	# 	return redirect('home.html')

class ProfileView(CreateView):
	fields = ('fullname','location','birth_date','gender','phone','image','email')
	model = models.Profile
	template_name = 'registration.html'

	#@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ProfileView, self).dispatch(*args, **kwargs)

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return redirect('home.html')

class ProfileUpdateView(UpdateView):
	fields = ('fullname','location','birth_date','gender','phone','image','email')
	model = models.Profile
	template_name = 'registration.html'

	#@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ProfileUpdateView, self).dispatch(*args, **kwargs)

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return redirect('home.html')

	#@method_decorator(login_required)
	# def dispatch(self, *args, **kwargs):
	# 	return super(ProfileView, self).dispatch(*args, **kwargs)
	#
	# def form_valid(self, form):
	# 	obj = form.save(commit=False)
	# 	obj.user = self.request.user
	# 	obj.save()
	# 	return redirect('home.html')

class ProfileView1(CreateView):
	fields = ('fullname','location','birth_date','gender','phone','image','user')
	model = models.Profile
	template_name = 'registration1.html'

	#@method_decorator(login_required)
	# def dispatch(self, *args, **kwargs):
	# 	return super(ProfileView, self).dispatch(*args, **kwargs)
	#
	# def form_valid(self, form):
	# 	obj = form.save(commit=False)
	# 	obj.user = self.request.user
	# 	obj.save()
	# 	return redirect('home.html')
def gen1(camera):
	while True:
		frame = camera.get_frame1()
		yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n' )





def preview(request):
	# user_id = request.user
	# id=user_id.id
	# context = {}
	#
	# if request.method == "POST":
	# 	ip = request.POST['ip']
	# 	auth_uname = request.POST['auth_uname']
	# 	auth_pwd   = request.POST['auth_pwd']
	# 	camIP = "rtsp://%s:%s@%s/" %(auth_uname, auth_pwd, ip)
	# 	print(camIP)
	# 	repsone = gen1(VideoCamera(camIP))
	# 	return  StreamingHttpResponse(repsone,content_type='multipart/x-mixed-replace; boundary=frame')
	questions=None
	if request.method == 'POST':
		ip = request.POST.get('ip')
		#auth_uname = request.POST.get('auth_uname')
		#auth_pwd = request.POST.get('auth_pwd')
		questions="%s" %(ip)
		camIP=questions
		request.session['camIP'] = camIP
		return render(request, 'Index/Camera_Add.html',{'questions': questions,})
	# questions=None
	# if request.GET.get('ip'):
	# 	ip = request.GET.get('ip')
	# 	auth_uname = request.GET.get('auth_uname')
	# 	auth_pwd = request.GET.get('auth_pwd')
	# 	questions="rtsp://%s:%s@%s/" %(auth_uname, auth_pwd, ip)
	# 	camIP=questions
	# 	request.session['camIP'] = camIP
	# 	return render(request, 'Index/Camera_Add.html',{'questions': questions,})


	return render(request,'Index/Camera_Add.html')

def video_streamer1(request):
	camIP = request.session.get('camIP')
	print(camIP)
	repsone = gen1(VideoCamera(camIP))
	return  StreamingHttpResponse(repsone,content_type='multipart/x-mixed-replace; boundary=frame')
