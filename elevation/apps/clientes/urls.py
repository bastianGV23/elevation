from django.conf.urls import url,include
from .views import lista_clientes,ModificarCliente,CrearCliente,DeleteCliente

urlpatterns = [
    url(r'^$', lista_clientes, name='menu'),
    url('modificar/(?P<pk>.+)/',ModificarCliente.as_view(), name="modificar"),
    url('eliminar/(?P<pk>.+)/',DeleteCliente.as_view(), name="eliminar"),
    url('crear/', CrearCliente.as_view(), name="crear"),
]