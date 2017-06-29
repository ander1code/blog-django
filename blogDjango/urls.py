from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from blogDjango import settings
from django.contrib.auth import login, logout, views as auth_views
from blog import views

admin.autodiscover()

urlpatterns = [
    url(r'^', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.do_login, name='do_login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
