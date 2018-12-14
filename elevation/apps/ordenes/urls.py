from django.conf.urls import url,include
from .views import lista_orden,crear_orden,DeleteOrden
urlpatterns = [
    url(r'^$', lista_orden, name='lista'),
    url('crear/', crear_orden, name='crear'),
    url('eliminar/(?P<pk>.+)/',DeleteOrden.as_view(), name="eliminar"),
]