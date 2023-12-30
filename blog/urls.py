from django.urls import re_path
from django.conf.urls.static import static
from blogdjango import settings
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'create/$', views.create, name='create'),
    re_path(r'show/(?P<id>\d+)/$', views.show, name='show'),
    re_path(r'edit/(?P<id>\d+)/$', views.edit, name='edit'),
    re_path(r'delete/(?P<id>\d+)/$', views.delete, name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
