from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='Index'
urlpatterns = [
 	url(r'^addcamera/',views.AddcameraView.as_view(), name='addcamera'),
 	url(r'^video_streamer/(?P<camID>\d+)',views.video_streamer, name='video_streamer'),
    url(r'^video_streamer1/',views.video_streamer1, name='video_streamer1'),
 	url(r'^cameras/',views.cameras_list, name='cameras_list'),
 	url(r'^deletecamera/',views.deletecamera, name='deletecamera'),
    url(r'^notification/',views.notification, name='notification'),
    url(r'^image/',views.image, name='image'),
    url(r'^cameradetails/',views.cameradetails, name='cameradetails'),
    url(r'^profile/',views.ProfileView.as_view(), name='profile'),
    url(r'^profile1/',views.ProfileView1.as_view(), name='profile1'),
    url(r'^profiledetail/(?P<pk>\d+)/$',views.ProfileDetailView.as_view(), name='profiledetail'),
    url(r'^profileupdate/(?P<pk>\d+)/$',views.ProfileUpdateView.as_view(), name='profileupdate'),
    # url(r'^jump/',views.jump, name='jump'),
    #url(r'^sample/',views.sample11, name='sample11'),
    url(r'^home/',views.home, name='home'),
    url(r'^preview/',views.preview, name='preview'),

    # AddcameraView.as_view()

 ]# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
