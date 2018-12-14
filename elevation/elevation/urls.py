"""elevation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path
from apps.registration.views import registro,cambiar_contraseña
from apps.core.views import menuPrincipal
from django.conf.urls import url,include
from django.urls import path
from apps.clientes.views import lista_clientes

urlpatterns = [
    path('', include('pwa.urls')),
    path('admin/', admin.site.urls),
    url(r'^registrar', registro, name="registrar"),
    url(r'^menu', menuPrincipal, name="menu"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    url(r"^$", registro, name=""),
    url(r'^contraseña/$', cambiar_contraseña, name='contraseña'),
    url(r'^clientes/', include(('apps.clientes.urls','clientes')), name='clientes'),
    url(r'^asignaciones/', include(('apps.asignacion.urls','asignaciones')), name='asignaciones'),
    url(r'^ordenes/', include(('apps.ordenes.urls','ordenes')), name='ordenes'),
]
