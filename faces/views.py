from django.shortcuts import render
from .models  import Facedetail
from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse,HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic.edit import CreateView ,UpdateView

@login_required
def faceprofile(request):
	context={}
	user_id=request.user
	id=user_id.id
	face=Facedetail.objects.filter(user_id=id)
	context.update({'face':face})
	return render(request,'faces/faceprofile.html',context)

class Faceprofilecreateview(CreateView):
	fields = ('name','image','video')
	model = Facedetail
	#template_name = 'registration.html'

	#@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(Faceprofilecreateview, self).dispatch(*args, **kwargs)

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return redirect('/home/')