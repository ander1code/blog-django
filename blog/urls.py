from django.conf.urls import url, include
from django.conf.urls.static import static
from blogDjango import settings
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'criar/$', views.criar, name='criar'),
    url(r'show/(?P<id>\d+)/$', views.show, name='show'),
    url(r'editar/(?P<id>\d+)/$', views.editar, name='editar'),
    url(r'excluir/(?P<id>\d+)/$', views.excluir, name='excluir')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
