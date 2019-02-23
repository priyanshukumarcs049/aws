from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from Index.views import (AddcameraView, LiveView)

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api/v1/', include('Index.api_urls')),
    url(r'', include('Index.urls')),
    url(r'', include('faces.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    url('', TemplateView.as_view(template_name='home.html'), name='home'),#registration/login.html
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
'''
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('Index.urls')),
]
'''
