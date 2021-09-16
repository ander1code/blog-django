from django.urls import re_path
from django.conf.urls.static import static
from blogdjango import settings
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'criar/$', views.criar, name='criar'),
    re_path(r'show/(?P<id>\d+)/$', views.show, name='show'),
    re_path(r'editar/(?P<id>\d+)/$', views.editar, name='editar'),
    re_path(r'excluir/(?P<id>\d+)/$', views.excluir, name='excluir')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
