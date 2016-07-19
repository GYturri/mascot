from django.conf.urls import url
from .views import Nuevo, Detalle

urlpatterns = [
	url(r'^nueva/$', Nuevo.as_view(), name='nuevo'),
	url(r'^detalle/(?P<slug>\d+)/$', Detalle.as_view(), name='detalle'),
	#url(r'^buscar/$', Buscar.as_view(), name='buscar'),
]