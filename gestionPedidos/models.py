from django.db import models

# Create your models here.


class Articulo(models.Model):

    nombre = models.CharField(max_length=80)
    precio = models.FloatField()
    stock = models.IntegerField()
    seccion = models.CharField(max_length=50)


class Cliente(models.Model):

    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)
    email = models.EmailField()
    telefono = models.IntegerField()
    compras = models.IntegerField()
    comentarios = models.CharField(max_length=120)


class Pedido(models.Model):

    cantidad = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    pagado = models.BooleanField()

# no es necesario agregar los constructores ya que django se encarga de esto
