from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='faces'
urlpatterns = [
 	url(r'^faceprofile/',views.faceprofile, name='faceprofile'),
    url(r'^faceprofilecreate/',views.Faceprofilecreateview.as_view(),name='faceprofilecreate'),


    # AddcameraView.as_view()

 ]# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
