from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from blogDjango import settings
from django.contrib.auth import views as autent_views


admin.autodiscover()

urlpatterns = patterns('blog.views',
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', autent_views.login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/', autent_views.logout, {'next_page':'/blog'}, name='logout'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
