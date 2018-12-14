from django.shortcuts import render, redirect
from .forms import AsignacionForm
from .models import Asignacion
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.urls import reverse_lazy
@login_required
def crear_asignacion(request):
    if request.method == 'POST':
        form = AsignacionForm(request.POST)
        if form.is_valid():
            asignar = form.save()
            return redirect('asignaciones:lista')
    else:
        form = AsignacionForm()
    return render(request, 'Principal/asignacion/asignacion.html', {'form': form})
@login_required
def lista_asignacion(request):
    asigna = Asignacion.objects.all()
    return render(request, 'Principal/asignacion/asignaciones.html',{'asigna':asigna})
class DeleteAsignacion(DeleteView):
    model = Asignacion
    template_name = "Principal/asignacion/eliminar.html"
    form_class = AsignacionForm
    success_url = reverse_lazy('asignaciones:lista')   