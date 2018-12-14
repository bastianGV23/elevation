from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.nombre + ' ' + self.direccion + ' ' + self.ciudad + ' ' + self.comuna + ' ' + self.email 


      