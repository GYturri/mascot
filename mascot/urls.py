from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as myloginview

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home/home.html'), name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    #url para redireccion si no esta logeado
    url(r'^login/$', myloginview.login, {'template_name':'home/login.html'}, name='login'),
    url(r'^cerrar/$', myloginview.logout_then_login, name='logout'),
    url(r'^inicio/', include('usuarios.urls', namespace="usuario")),
    url(r'^mascota/', include('pets.urls', namespace="mascota")),
    url(r'^admin/', admin.site.urls),
    url(r'^add_email/', 'usuarios.views.get_email'),
]
