"""mascot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as myloginview

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home/home.html'), name='home'),
    #url para redireccion si no esta logeado
    url(r'^login/$', myloginview.login, {'template_name':'home/login.html'}, name='login'),
    url(r'^cerrar/$', myloginview.logout_then_login, name='logout'),
    url(r'^inicio/', include('usuarios.urls', namespace="usuario")),
    url(r'^mascota/', include('pets.urls', namespace="mascota")),
    url(r'^admin/', admin.site.urls),
]
