"""blogdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
from django.urls import re_path
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from blogdjango import settings
# from django.contrib.auth import login, logout, views as auth_views

from blog import views

admin.autodiscover()

urlpatterns = [
    re_path(r'^', include('blog.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^login/$', views.do_login, name='do_login'),
    re_path(r'^logout/$', views.do_logout, name='do_logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
