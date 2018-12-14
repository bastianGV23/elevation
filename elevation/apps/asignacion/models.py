from django.db import models
from apps.core.models import User
from apps.clientes.models import Cliente

# Create your models here.
class Asignacion(models.Model):
    cli = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(User, on_delete=models.CASCADE)
