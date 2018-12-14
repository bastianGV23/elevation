from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from apps.ordenes.models import Orden
from apps.core.models import User
from apps.asignacion.models import Asignacion
from .forms import OrdenForm
from django.views.generic import DeleteView
# Create your views here.
@login_required
def lista_orden(request):
    if request.user.is_superuser:
        orden = Orden.objects.all()
    else:
        us = request.user
        orden = Orden.objects.filter(tecnico_id = us.id)
    return render(request, 'Principal/ordenes/ordenes.html',{'orden':orden})
@login_required
def crear_orden(request):
    if request.method == 'POST':
        us = request.user
        form = OrdenForm(request.POST)
        if form.is_valid():
            orden = form.save(commit = False)
            orden.tecnico = request.user
            orden = form.save()
            return redirect('ordenes:lista')
    else:
        form = OrdenForm()
    return render(request, 'Principal/ordenes/orden.html', {'form': form})
class DeleteOrden(DeleteView):
    model = Orden
    template_name = "Principal/ordenes/eliminar.html"
    success_url = reverse_lazy('ordenes:lista')  