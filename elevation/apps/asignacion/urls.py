from django.conf.urls import url,include
from .views import lista_asignacion,crear_asignacion,DeleteAsignacion
urlpatterns = [
    url(r'^$', lista_asignacion, name='lista'),
    url('crear/', crear_asignacion, name='crear'),
    url('eliminar/(?P<pk>.+)/',DeleteAsignacion.as_view(), name="eliminar"),
]
   