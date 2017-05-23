from django.conf.urls import patterns, url
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('blog.views',
    url(r'^$', views.home, name='home'),
    url(r'criar/$', views.criar, name='criar'),
    url(r'show/(?P<id>\d+)/$', views.show, name='show'),
    url(r'editar/(?P<id>\d+)/$', views.editar, name='editar'),
    url(r'excluir/(?P<id>\d+)/$', views.excluir, name='excluir')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
