from django.db import models
from datetime import datetime 
from apps.clientes.models import Cliente
from apps.core.models import User
# Create your models here.
class Orden(models.Model):
    nombreReceptor = models.CharField('Nombre del receptor',max_length=30)
    cliente =   models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(User, on_delete=models.CASCADE)
    id_ascensor = models.CharField('ID ascensor',max_length=10,unique=True)
    piezas = models.CharField('Piezas cambiadas',max_length=30)
    reparaciones = models.CharField('Reparaciones efectuadas',max_length=50)
    fallas = models.CharField('Fallas detectadas',max_length=50)
    hora_inicio = models.DateTimeField(auto_now_add=True)
    hora_termino = models.DateTimeField(auto_now=True)
    modelo_asc = models.CharField('Modelo de ascensor',max_length=50)
    email = models.EmailField(max_length=30)
    def __str__(self):
        return self.nombreReceptor + ' ' + self.id_ascensor + ' ' + self.piezas + ' ' + self.reparaciones + ' ' + self.email + ' ' + self.modelo_asc + ' ' + self.fallas
    

      