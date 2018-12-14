from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .forms import clienteForm
from .models import Cliente
# Create your views here.
@login_required
def lista_clientes(request):
    cliLista = Cliente.objects.all()   
    return render(request, 'Principal/clientes/clientes.html',{'cliente':cliLista})

class CrearCliente(CreateView):
    model = Cliente
    template_name = "Principal/clientes/cliente.html"
    form_class = clienteForm
    success_url = reverse_lazy('clientes:menu')

class ModificarCliente(UpdateView):
    model = Cliente
    template_name = "Principal/clientes/cliente.html"
    form_class = clienteForm
    success_url = reverse_lazy('clientes:menu')

class DeleteCliente(DeleteView):
    model = Cliente
    template_name = "Principal/clientes/eliminar.html"
    success_url = reverse_lazy('clientes:menu')
