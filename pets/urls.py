from django.conf.urls import url
from .views import Nuevo

urlpatterns = [
	url(r'^nueva/$', Nuevo.as_view(), name='nuevo'),
	#url(r'^buscar/$', Buscar.as_view(), name='buscar'),
]